'''First try of the PySpark.'''
# pylint: disable=pointless-string-statement

import sys
from pyspark.sql import SparkSession

"""
# data example
+-----+------+-----+   
|State| Color|Count|   
+-----+------+-----+   
|   TX|   Red|   20|   
|   NV|  Blue|   66|   
|   CO|  Blue|   79|   
|   OR|  Blue|   71|   
|   WA|Yellow|   93|   
+-----+------+-----+ 
"""

if __name__ == "__main__":
    if len(sys.argv) != 2:
        # show that necessary to pass the csv file
        print("Usage: mnmcount <file>", file=sys.stderr)
        sys.exit(-1)

    # creating a spark session
    spark: SparkSession = (
        SparkSession
        .builder
        .appName("PythonMnMCount")
        .getOrCreate()
    )

    # get the csv file path
    mnm_file = sys.argv[1]
    # create a df
    mnm_df = (
        spark.read.format('csv')
        .option('header', 'true')
        .option('inferSchema', 'true')
        .load(mnm_file)
    )
    mnm_df.show(5, truncate=False) # truncate - means crop the row or not

    # count the mnms by states
    count_mnm_df = (
        mnm_df
        .select(['State', 'Color', 'Count'])
        .groupBy(['State', 'Color'])
        .sum('Count')
        .orderBy('sum(Count)')
    )
    count_mnm_df.show(60, truncate=False)
    print(f'Total rows in the count df: {count_mnm_df.count()}')

    # count the mnms only for CA
    ca_mnm_df = (
        mnm_df
        .select('*')
        .where(mnm_df.State == 'CA') # condition. State is only CA
        .groupBy(['State', 'Color'])
        .sum('Count')
    )
    ca_mnm_df.show()
