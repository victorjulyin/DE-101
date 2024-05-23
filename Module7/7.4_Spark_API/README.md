## Definitions
* RDD (Resilent Distributed Datasets) - low level data formatting. Main data object in Spark
    - can't be changed. But possible to transform it to another RDD with changes.
* DataFrame - an API over RDD. Like an evolution over the RDD.
    - Adds the data schema and columns
    - We can see it as a table

## DataFrame and schema:
* Always better to define the schema of a DataFrame because:
    - Spark doesn't need to scan the data to get the types of columns (performance)
    - Easier to check the data quality. Because if there is data type in column that doesn't match with the schema, Spark raises an exception

* Two types of schema definition:
    - Programmatically:
        ```
            from pyspark.sql.types import *
            schema = StructType([ScructField("author", StringType(), False), ScructField("title", StringType(), False), ScructField("pages", IntegerType(), False)])
        ```
    - Data Definition Language (DDL):
        ```
            schema = 'author STRING, title STRING, pages INT'
        ```

## When to use RDD:
    - RDD is already used in the project
    - Necessary to optimize the code very detailed
    - Necessary to givevery accurate commands to Spark

## Catalyst Optimizer
Creates an Execution Plan based on a query
Includes:
    - Analyse
    - Logical optimization
    - Physical optimization
    - Code generation