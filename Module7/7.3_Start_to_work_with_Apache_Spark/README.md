## Definitions
* Apache Spark - in simple words it is a transformation tool. Spark extracts and transforms data, but not stores it.
-------------
* Spark Application - the app that includes Driver and Executors.
* Spark Driver - coordinates the whole process.
* Spark Executor - runs dedicated calculations.
* Spark Session - initialisation of Spark. Creation of a dedicated system for the calculations.
* Cluster Manager - resource manager (YARN, Mesos etc).
* Job - goal of the DAG execution.
* Stage - calculation stages job divides on.
* Task - a certain piece of work that is gonna be done on a Executor

## When we need it
    - There is a classic DWH but it is too large and can't handle the load.
    - There is a Big Data or Data Lake and we want so we can process the data with Spark without a DWH.
    - We need streaming (Spark Structured Streaming).
    - ML purposes.
    - We just love Python.

## Use possibilities
    - Spark localhost (standalone)
    - Spark + Hadoop
    - Spark Docker
    - Managed Spark (Databricks, Amazon Glue)
    - Spark Kubernetes

## First try of Spark
    - I've written the code. Run the provided command to see the result:
        ```
        python Module7\7.2_Start_to_work_with_Apache_Spark\spark_script.py Module7\7.2_Start_to_work_with_Apache_Spark\mnm_dataset.csv
        ```