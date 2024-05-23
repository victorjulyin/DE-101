'''Answering the questions related to the San-Francisco fire guard calls.'''

from pyspark.sql import SparkSession, functions as F

if __name__ == '__main__':
    spark: SparkSession = (
        SparkSession
        .builder
        .appName('SF_fire_guard')
        .getOrCreate()
    )

    file_path = "Module7/7.4_Spark_API/practice/sf-fire-calls.csv"

    df = spark.read.csv(
        file_path,
        header=True, # if csv file has the first line with the column names than set True
        inferSchema=True # Sets the types of columns automatically.
                         # Spark reads the csv file and checks the types.
                         # If "False", it is faster, but all the types are gonna be string
    )

# Q-1) How many distinct types of calls were made to the Fire Department?
# To be sure, let's not count "null" strings in that column.
    print('----------------------')
    print('Q-1) How many distinct types of calls were made to the Fire Department?')
    q1 = (
        df
        .select('CallType')
        .where('CallType is not null')
        .distinct()
        .count()
    )

    print(f'Answer: {q1}.')


# Q-2) What are distinct types of calls were made to the Fire Department?
    print('----------------------')
    print('Q-2) What are distinct types of calls were made to the Fire Department?')
    q2 = (
        df
        .select('CallType')
        .where('CallType is not null')
        .distinct()
        .collect() # this transforms the dataframe to a list of Row() objects
    )
    call_types = [i.asDict().get('CallType') for i in q2] # that's how we parse the Row() objects
    print(f'Answer: {call_types}')


# Q-3) Find out all response or delayed times greater than 5 mins?
# Rename the column Delay - > ReponseDelayedinMins
# Returns a new DataFrame
# Find out all calls where the response time to the fire site was delayed for more than 5 mins
    print('----------------------')
    print('Q-3) Find out all response or delayed times greater than 5 mins?')
    q3 = (
        df
        .selectExpr('Delay AS ResponseDelayedinMins') # if necessary to use alias
        .where('ResponseDelayedinMins > 5')
        .count()
    )
    print(f'Answer: {q3}')


# Q-4a) What zip codes accounted for most common calls?
# Let's investigate what zip codes in San Francisco accounted for most fire calls and what type where they.
# Filter out by CallType
# Group them by CallType and Zip code
# Count them and display them in descending order
# It seems like the most common calls were all related to Medical Incident, and the two zip codes are 94102 and 94103.
    print('----------------------')
    print('Q-4a) What zip codes accounted for most common calls?')
    cols = ['CallType', 'Zipcode']
    q4a = (
        df
        .select(cols)
        .where('CallType is not Null')
        .groupBy(cols)
        .count()
        .sort('count', ascending=False)
    )

    q4a.show(5)


# Q-4b) What San Francisco neighborhoods are in the zip codes 94102 and 94103
# Let's find out the neighborhoods associated with these two zip codes.
# In all likelihood, these are some of the contested neighborhood with high reported crimes.
    print('----------------------')
    print('Q-4b) What San Francisco neighborhoods are in the zip codes 94102 and 94103?')
    q4b = (
        q4a
        .limit(2)
        .join(df, 'Zipcode')
        .select(['Zipcode', 'Neighborhood'])
    )

    q4b.show()
# Q-5) What was the sum of all calls, average, min and max of the response times for calls?
# Let's use the built-in Spark SQL functions to compute the sum, avg, min, and max of few columns:
# Number of Total Alarms
# What were the min and max the delay in response time
# before the Fire Dept arrived at the scene of the call
    print('----------------------')
    print('Q-5) What was the sum of all calls, average, min and max of the response times for calls?')
    q5 = (
        df
        .agg(
            F.sum('Delay').alias('sum_delay'),
            F.avg('Delay').alias('avg_delay'),
            F.min('Delay').alias('min_delay'),
            F.max('Delay').alias('max_delay')
        )
    )
    q5.show()

# ** Q-6) What week of the year in 2017 had the most fire calls?**
# Note: Week 1 is the New Years' week and week 25 is the July 4 the week.
# Loads of fireworks, so it makes sense the higher number of calls.
    print('----------------------')
    print('Q-6) What week of the year in 2018 had the most fire calls?')
    q6 = (
        df
        .select(['CallNumber', 'CallDate'])

        # add column
        # convert string date to datetime
        .withColumn('ObjCallDate', F.to_date('CallDate', 'MM/dd/yyyy'))
        .drop('CallDate')

        # filtering
        .where('year(ObjCallDate) = 2018')

        # add weekofyear
        .withColumn('WeekOfYear', F.weekofyear('ObjCallDate'))
        .drop('ObjCallDate')

        # group
        .groupBy('WeekOfYear')
        .count()

        # sort
        .orderBy('count', ascending=False)
    )
    q6.show(10)

# ** Q-7) What neighborhoods in San Francisco had the worst response time in 2018?**
# It appears that if you living in Presidio Heights, the Fire Dept arrived
# in less than 3 mins, while Mission Bay took more than 6 mins.
    print('----------------------')
    print('Q-7) What neighborhoods in San Francisco had the worst response time in 2018?')
    q7 = (
        df
        .select(['Neighborhood', 'Delay', 'City'])
        .where('City = "SF"')
        .groupBy('Neighborhood')
        .agg(
            F.avg('Delay').alias('avg_delay'),
        )
        .sort('avg_delay', ascending=[False])
        .limit(5)
    )
    q7.show()


# ** Q-8a) How can we use Parquet files or SQL table to store data and read it back?**
    print('----------------------')
    print('Q-8a) How can we use Parquet files or SQL table to store data and read it back?')

    PARQUET_PATH = 'Module7/7.4_Spark_API/practice/my_parquet_file'
    q8a = (
        df
        .select(['Neighborhood', 'Delay', 'City'])
        .limit(10)
    )

    q8a.show()

    q8a.write.parquet(PARQUET_PATH)


# ** Q-8c) How can read data from Parquet file?**
# Note we don't have to specify the schema here since it's stored as part
# of the Parquet metadata
    print('----------------------')
    print('Q-8c) How can read data from Parquet file?')
    df_from_parquet = spark.read.parquet(PARQUET_PATH)

    df_from_parquet.show()
