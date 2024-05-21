## Managed and Unmanaged Spark
### Managed Spark
    * Managed Spark processes Metadata and files with data. It means that it can delete the data from the source.
    ```
        # this deletes the data from source (S3, MySQL, CSV) in Managed Spark
        df.sql('DROP TABLE table_name')
    ```
    * Options to create the Managed Spark table: 
    ```
        # option 1
        spark.sql("CREATE TABLE managed_us_delay_flights_tbl (date STRING, delay INT,  \
        distance INT, origin STRING, destination STRING)")

        # option 2
        # Path to our US flight delays CSV file 
        csv_file = "departuredelays.csv"
        # Schema as defined in the preceding example
        schema="date STRING, delay INT, distance INT, origin STRING, destination STRING"
        flights_df = spark.read.csv(csv_file, schema=schema)
        flights_df.write.saveAsTable("managed_us_delay_flights_tbl")
    ```

### Unmanaged Spark
    * Unmanaged Spark processes only Metadata. It means that the source data is safe. Preferable in production.
    ```
        # doesn't delete the data from source (S3, MySQL, CSV) in Unmanaged Spark. Deletes only metadata
        df.sql('DROP TABLE table_name')
    ```
