
## Redshift create table options

### Distribution key
    * Possibility to choose how to distribute the data between clusters/nodes:
        * All - copy the table between all of the nodes. May be good for small and constant tables.
        * Even - default distribution style. No joins
        * Distribution Key - large tables, have joins, star schema. Best to use a primary key as a key here

### Sort key
    * Compound - made up all of the columns listed in the sort key definition, in the order they are listed.
    * Interleaved - gives equal weight to each column, or subset of columns, in the sort key.

### Constrains
    * Enforced (actually works):
        * Null / Not null
    * Not enforced:
        * Primary key
        * Foreign key
        * Unique
        * References

### Compression
    * Storing less data lowers cost
    * Reduce disk I/O
    * Encoding on each column
    * Possible to ask Redshift to use optimal encoding

### Copy Command
    * Fast option to add the whole table to Redshift. Instead of inserting row by row just add the whole table (csv file) to Redshift.
    * Possible to Copy with manifest (json file with configurations). It allows to:
        * Load required files only
        * Load files from different buckets
        * Load files with different prefix
        * JSON format

### Bulk Insert
    * Very fast operation. Works when use construction: insert into <table_name> (select * from some_table;)

### Error checking
    * There are two tables where the errors stored. It is possible to get the error from the by error_id:
        * STL_LOAD_ERRORS
        & STL_LOADERROR_DETAIL

### Workload Management (WLM)
    * Rules to route queries to queues. Necessary to use it when there are a lot of users of Redshift

### Vacuum
    * Re-sorts rows and reclaims space in a specified table or all tables in the current database. Necessary to run this commands because when rows are Deleted or Updated, these changes are not applying automatically in Redshift.
        * Vacuum full:
            * Default vacuum command. Sorts the specified table, actually deletes and updates rows
        * Vacuum sort only:
            * Only sorts data in disc. May be used when you don't need to free the space but want to sort the data on the disc (faster queries)
        * Vacuum Delete Only:
            * Only reclaims space that changed as a result of a Delete or Update command. 

### Analyze
    * Updates table statistics for use by the query planner

### Top 10 performance tuning techniques
    * Precomputing results with Redshift meterialized views
    * Handling bursts of workload with concurrency scailing and elastic resize
    * Using the Redshift Advisor to minimize administrative work
    * Using Auto WLM with priorities to increase throughput
    * Taking advantage of Redshift data lake integration
    * Improving the efficiency of temporary tables
    * Using QMR and Amazon CloudWatch metrics to drive additional performance improvements
    * Federated queries connect the OLAP, OLTP and data lake worlds
    * Maintaining efficient data loads
    * Using the latest Amazon Redshift drivers from AWS
