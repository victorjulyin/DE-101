## The plan

  1) [Context](#context)
    * [What context is](#what-context-is)
    * [Access](#access)
    * [Example](#example)
  2) [Xcom](#xcom)
  3) [General example]


## Context
### What context is

Context - a set of fields (a lot of fields) that is creating during the initialization of a task.

For example:
  * Which DAG does this task belong to
  * Planned time of execution


### Access

    from airflow import DAG 
    from datetime import datetime 
    from airflow.operators.python_operator import PythonOperator 
    
    default_args = {"owner": "airflow", "start_date": datetime(2018, 10, 1)} 
    dag = DAG(dag_id="dag", default_args=default_args, schedule_interva="@daily") 
    
    # This function is using context
    def _print_exec_date(**kwargs):          # "kwargs" = context in this case
        print("Контекст", kwargs)            
        
    print_exec_date = PythonOperator( 
        task_id="print_exec_date", 
        python_callable=_print_exec_date, 
        dag=dag, )



### Example

    from airflow import DAG
    from airflow.operators.python_operator import PythonOperator
    from datetime import datetime


    def my_func(hello, date, **kwargs):
      print(hello)
      print(date)
      print(kwargs['task'])      # show task name using context


    dag = DAG('dag', schedule_interval='@daily', 
              start_date=datetime(2021, 1, 1),       # datetime() - function to insert date
              end_date=datetime(2024, 1, 1))

    python_task    = PythonOperator(
      task_id='python_task', 
      python_callable=my_func,
      op_kwargs= {
        'hello': str("Hello World"),     
        'date': "{{ ds }}"             # show date of the task execution using macros jinja2
        },
        dag=dag
      )



## Xcom

Tasks are executing in different processes or even on different machines. So it is impossible to get result of a task in another execution stream.
In this case, there are few options to do it:

  * Generate temporary files (if we use one machine)
  * Queue of messages with a web access
  * Data base and DW
  * Xcom with S3 backend (relevant for version >2.0)

In the case of metadata, use **Xcom**. It is an interface that uses acess key-value. It is like a table inside of airflow. 

### Example


    from airflow import DAG
    from datetime import timedelta
    from airflow.utils.dates import days_ago
    from airflow.operators.bash import BashOperator

    dag = DAG('dag',schedule_interval=timedelta(days=1), start_date=days_ago(1))

    downloading_data = BashOperator(
        task_id='downloading_data',
        bash_command='echo "Hello, I am a value!"',   # bash output "Hello, I am a value!" will go to xcom
        do_xcom_push=True,    # because of this argument ("push data to xcom")
        dag=dag
    )

    fetching_data = BashOperator(
        task_id='fetching_data',
        # You can also send data to xcom by jinja
        bash_command="echo 'XCom fetched: {{ ti.xcom_pull(task_ids=[\'downloading_data\']) }}'",
        do_xcom_push=False,       # result will not be sended to xcom 
        dag=dag
    )

    downloading_data >> fetching_data


Extra [Xcom materials](https://khashtamov.com/ru/apache-airflow-xcom/)


## General example

    import sqlite3 as sl
    import pandas as pd
    from airflow import DAG
    from datetime import timedelta
    from airflow.utils.dates import days_ago
    from airflow.operators.python_operator import PythonOperator
    from datetime import datetime
    
    
    dates_list = '2021-01-01'
    conn = sl.connect('my-test.db')
    cursor = conn.cursor()
    
    def extract_currency(base='EUR', symbols='USD', format='csv', if_exists='replace', **kwargs):
      ds = kwargs['ds']
      url = f'https://api.exchangerate.host/timeseries?start_date={ds}&end_date={ds}&base={base}&symbols={symbols}&format={format}'
      response = pd.read_csv(url).to_dict()['rate'][0]
      return response
    
    def extract_data(date, conn=conn, if_exists='replace'):
      url = f'https://raw.githubusercontent.com/dm-novikov/stepik_airflow_course/main/data_new/{date}.csv'
      df = pd.read_csv(url, squeeze=True)
      df.to_sql('data', conn, if_exists=if_exists, index = False)
    
    def pull_from_xcom(task_name, conn=conn, if_exists='replace', **kwargs):
      ti = kwargs['ti']
      result = ti.xcom_pull(task_ids=task_name)
      print(result)
    
    def sql_query(sql, conn=conn, cursor=cursor):
      cursor.execute(sql)
      conn.commit()
      d = cursor.fetchall()
      return d

    def create_tables(conn=conn):
      sql_query('DROP TABLE IF EXISTS data') 
      sql_query('DROP TABLE IF EXISTS currency')
      sql_query('DROP TABLE IF EXISTS join_data')  

      sql_query('CREATE TABLE IF NOT EXISTS currency (currency text, value float, date date)') 
      sql_query('CREATE TABLE IF NOT EXISTS data (date date, code text, rate float, base text, start_date date, end_date date)') 
      sql_query('CREATE TABLE IF NOT EXISTS join_data (val_eur float, val_usd, date date)') 


    def select_data(conn=conn):
      print('STARTED select_data func')
      sql_query('''INSERT INTO join_data
                   SELECT value, round(value * CAST(replace(rate, ',', '.') as float), 2), currency.date
                   FROM currency INNER JOIN data
                   ON currency = base AND currency.date = data.date
                ''')
  
      # Clean temp tables CURRENCY, DATA
      sql_query('DROP TABLE IF EXISTS currency')
      sql_query('DROP TABLE IF EXISTS data')

      # fetch data from JOIN_DATA for a certain date
      report = sql_query(f"SELECT * FROM join_data")
      print(report)
      print('FINISHED select_data func')



    dag = DAG('dag',schedule_interval=timedelta(days=1), start_date=days_ago(1))
    #dag = DAG('dag',schedule_interval=timedelta(days=1), start_date=datetime(21,1,1), end_date=datetime(21,1,4))
  

    # Create tables
    create_tables = PythonOperator(task_id="create_tables",
                                       python_callable=create_tables,
                                       op_kwargs={},
                                       dag=dag
                                      )


    # Download currency rate and insert into xcom
    download_currency = PythonOperator(task_id="download_currency",
                                       python_callable=extract_currency,
                                       provide_context=True,
                                       do_xcom_push=True,        # PUSH RESULT TO XCOM
                                       dag=dag
                                      )


    # Download github Data and insert into table
    download_data = PythonOperator(task_id="download_data",
                                       python_callable=extract_data,
                                       op_kwargs={"date": dates_list},
                                       provide_context=True,
                                       dag=dag
                                      )

    pull_currency = PythonOperator(task_id="pull_currency",
                                       python_callable=pull_from_xcom,
                                       op_kwargs={"task_name": "download_currency"},
                                       provide_context=True,
                                       do_xcom_push=False,        # DON'T PUSH RESULT TO XCOM
                                       dag=dag
                                      )


    create_tables >> download_currency >> download_data >> pull_currency
