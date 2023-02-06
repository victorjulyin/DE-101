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

Operator - task that is inside of a DAG

A sample:
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

### Types of operators

  * Transfer - transfer data from one source to another
  * Action - "Do this". Like functions
  * Sensor - checks existance of something (for example - is there some file on a computer?)


## Dependencies

M2_2
M2_3
