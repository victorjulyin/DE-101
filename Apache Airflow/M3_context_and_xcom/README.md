## The plan




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



# Xcom

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

