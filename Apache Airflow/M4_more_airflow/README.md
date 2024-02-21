## The plan






## Architecture

**m4_1**

Airflow is a module system consisting of 5 main components:

  * Folder with DAGs (directory where pipeline scripts are stored)
  * Metadata base (DW to store info about running tasks)
  * Web-server (airflow web-interface)
  * Scheduler (it does the main work, checks and refreshes DAGs, looks after schedule)
  * Executor (launching mechanism, there are 2 types)



### DAG launching process

#### First of all, *Scheduler* scans *DAG folder* recursively to find out when and what should be executed. Checks DAGs for an access and refresh.

**m4_2**

#### *Scheduler* decided to run DAG => *Executor* is starting. Executor is responsible for running tasks.

**m4_3**

#### Then *Worker* is taking a task from a pool and starting the execution. Different situation is possible for *Sensors*  - task repeating (Rescheduler)

**m4_4**

#### Next actions depend on the task status. Success - thread stops, failed - task may fail or repeat (depends on settings).

**m4_5**

### Executors and pools

#### Executors

There are two types of executors that launch tasks locally:
  1) **Sequential Executor (default)** - uses SQLite as backend. Can't launch tasks parallelly, this realisation is not good for a real use, just as a test.
  2) **Local Executor** - requires client-server data base for backend, can work paralelly. In the simplest version, you can put it together with PostgreSQL.

If you want to place airflow on several machines, use these:
  1) **Celery Executor** - allows to scale workers on a few machines
  2) **Kubernetes Executor** - allows to deploy airflow in a Kuber claster

Also there are other options, for example **Dask Executor** and **Debug Executor**.


#### Pools

Pools - is a mechanism for limiting task parallelism. For example, we have a DAG with hundreds of parallel tasks, there is a risk to overload the server. That's what pools are for, they can be created manually and specified in the dag settings.
For example, you can create a pool for 10 threads (default - 128), then more than 10 tasks will not be loaded at a time.

    aggregate_db_message_job = BashOperator(
      task_id='task_1',
      pool='non_default_pool',
      bash_command="echo 1",
      dag=dag,
    )



## Web Interface

### Basic information

The Airflow interface is intended primarily for viewing the status of our tasks and logs.
Besides, it lets to mass relaunch tasks, edit global variables, manage access etc.

**m4_6**


The most useful tabs:
    * DAGs - list of all DAGs
    * Browse - logs
      * Task Instances - the place where we can see all our tasks and their statuses. Also we can change the status manually here
    * Admin - configs, global variables, xcom
      * Variables - we can create global variables here (we'll have an access to them from everywhere)
      * Connections - info about our data sources (hosts, passwords, logins etc)
      * Pools - tool to restrict executable threads 
      * Xcom - temporary storage for data from tasks
    * Security - info about airflow users
    

#### How to get access to a connection

    # Пример доступа к переменной connection
    from airflow.hooks.base_hook import BaseHook
    host = BaseHook.get_connection("postgres_default").host
    pass = BaseHook.get_connection("postgres_default").password


#### How to call a variable

    # access to a global variable example
    from airflow.models import Variable
    foo = Variable.get("key")




