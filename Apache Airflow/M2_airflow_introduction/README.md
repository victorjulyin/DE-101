**M2_1**
Airflow - a scheduler. And DAG is like a container for tasks.



## DAGs 

DAG - is a class. So when we create a DAG, we create a new object.

### Launching

There is no difference between next launching options:

  # Without "WITH":
  dag = DAG('dag', schedule_interval=timedelta(days=1), start_date=days_ago(1))

  # 'dag' - name of our DAG
  # 'schedule_interval' - launch frequency
  # 'start_date' - when to start (it can be past too)
  

  # By context manager:
  with DAG('dag', schedule_interval=timedelta(days=1), start_date=days_ago(1)) as dag: ...


### Optional DAG arguments

  * retries - repeat N times if DAG failed
  * on_failure_callback - calls some function if DAG failed (usually notifications by messengers)
  * trigger_rule - what to do if some task failed


## Operators

Operator - task that is inside of a DAG.
It is a class DAG object. So inside is just a Python code. We can create our own Operators.


  # Python operator sample (action)

  def print_context(ds):
    return 'Hello World!'

  run_this = PythonOperator(
    task_id='print_the_context',
    python_callable=print_context,
    op_kwargs={
            'url': 'https://raw.githubusercontent.com/file25',
            'tmp_file': '/tmp/file.csv'}
    dag=dag
  )

  # Or a bash-operator (action)

  BashOperator(task_id='echo_1', bash_command='echo 1',dag=dag)


  # Operator to transfer Data from MySQL to GCS (transfer)
  upload = MySQLToGCSOperator(
    task_id='mysql_to_gcs', 
    sql=SQL_QUERY, 
    bucket=GCS_BUCKET, 
    filename=FILENAME, 
    export_format='csv'
  )

  # Operator that checks existing of a file on a disk (sensor)
  sensor_task = FileSensor(
     task_id="my_file_sensor_task", 
     poke_interval=30, 
     fs_conn_id=PATH, 
     filepath=FILE_OR_NAME
  )



We use operators for a description of certain actions:
  * Download Data from DB
  * Send an email
  * Execute a bash-command
  * Execute a Python code



### Types of operators

  * Transfer - transfer data from one source to another
  * Action - "Do this". Like functions
  * Sensor - checks existance of something (for example - is there some file on a computer?)


## Dependencies

M2_2
M2_3


## DAG + operators creation example

  from airflow import DAG
  from datetime import timedelta
  from airflow.utils.dates import days_ago
  from airflow.operators.bash_operator import BashOperator
 
  # Create an object of DAG class
  dag =  DAG('dag',schedule_interval=timedelta(days=1), start_date=days_ago(1))

  # Create a few steps, that will execute bash-commands in parallel
  t1 = BashOperator(task_id='echo_1', bash_command='echo 1',dag=dag)
  t2 = BashOperator(task_id='echo_2', bash_command='echo 2',dag=dag)

This approach allows us to build declarative-style pipelines.

**More about declarative and imperative approach:**
Imperative approach - build some chain of tasks but don't give exact values

  a = int(input())
  b = int(input())
  print(a + b)


Declarative approach - strictly specify the values to be used

  print (1+1)


