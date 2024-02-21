# How to set up an airflow?

## Airflow installation
    
    # 1 import necessary libs
    import os
    os.environ["AIRFLOW_HOME"] = "/content"



    # 2 Airflow installing
    !pip install 'apache-airflow[google,amazon,postgres]'
    
    # inside of the square brackets you can see additional packages that will be installed with an airflow
    # it is better to use it (when necessary) because it will install everything right
    # other options:
    !pip install 'apache-airflow[all]' # all packages
    !pip install 'apache-airflow[all_dbs]' # all data bases



    # 3 initialize data base
    !airflow db init
    
    # After a DB initialization we'll see files:
    #    - "airflow.db" - database, nothing interesting
    #    - logs - look at the bottom
    #    - "airflow.cfg" - Most important thing. This is the file where we can find all configurations for the airflow. All that the engine needs: Dag folder, executor, amount of DAGs in a queue in one time etc.
    #    - "webserver_config.py" - we can create an autenthification here or change the airflow web interface
    # Any parameter from airflow.cfg can be edited with a global variable, for example
        AIRFLOW_CORE_*variable_name* = ...
        AIRFLOW_CORE_DAGS_FOLDER = 'enter_the_path'



    # 4 create an Airflow user
    !airflow users create \
              --username admin \  
              --firstname admin \
              --lastname admin \
              --role admin \    # first user have to be "admin"
              --email admin@example.org \
              -p 12345


    # 5 turn on web-server
    !airflow webserver -p 18273 -D    # port should be different (it is just an example)
                                      # -D = daemon. It means it is launching asynchronously

    
    # 6 turn on scheduler (dag must be created)
    !airflow scheduler -D



    # 7 extra thing
    # airflow also stores logs of every dag launch. There is a lot of info. So we have two options:
    #  1) connect an external hard drive (it should be fast)
    #  2) connect airflow to an external storage like aws S3
    # don't forget to clean logs sometimes

    # some of the parameters that using for a cloud storage
    remote_logging = False
    remote_log_conn_id =
    remote_base_log_folder =


    # if we need to use some extra module:

    !pip install apache-airflow-providers-<PACKAGE>

    # for example:
    
    ### Telegram installing ### 
    
    # library for work with telegram
    !pip install python-telegram-bot
    
    # install http-provider and telegram-provider
    pip install apache-airflow-providers-http
    pip install apache-airflow-providers-telegram


## Plug-ins and notification

### Plug-ins

Airflow has a comfortable solution to store all code in one place. It is a folder named *plugins/*

Example:

plugins/
├── __init__.py
└── custom_plugin
    └── operators
        └── operator_1
        └── __init__.py
    └── hooks
        └── hook_1
        └── __init__.py
    └── sensors
        └── sensor_1
        └── __init__.py
    └── __init__.py


Also it is necessary to add this folder to PYHTONPATH and restart the scheduler
    import sys
    sys.path.append("/root/airflow/plugins")
    sys.path.append("/root/airflow/dags")

After that access to the plagin from file is gonna be like this:
    from custom_plugin.operators.operator_1 import CustomOperator


### Notification

Airflow knows how to handle events like failed or success. For example:

    from datetime import timedelta
    from airflow import DAG

    default_args = {
        'on_failure_callback': some_function, # Задача упала
        'on_success_callback': some_other_function, # задача успешно отработала
        'on_retry_callback': another_function, # Задача повторяется
    }
    with DAG(
        'tutorial',
        default_args=default_args,
        schedule_interval=timedelta(days=1),
        start_date=days_ago(2),
    ) as dag: pass

Example of the function that sends the notification message:

    def some_other_function(context):
        send_message = TelegramOperator(
            task_id='send_message_telegram',
            telegram_conn_id='telegram_id',
            text=context.get('task_instance').task_id)
        return send_message.execute(context=context)