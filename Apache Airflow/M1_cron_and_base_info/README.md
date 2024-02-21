## First Module plan

1) [Test task](#test-task)
2) [Theory](#theory)
3) [Final task - create a python pipeline](#python-pipeline-creation)

## Test task


<img src="https://github.com/victorjulyin/DE-101/blob/main/Apache%20Airflow/M1_cron_and_base_info/pics/M1_1.png" width=50% height=50%>


**The task: Load the Data from an external source  everyday and provide a revenue statistics in available sections. The report must come to the whole team mail at 10 am. Data should be saved in a local Data Base.**

## The Python solution

### We can use some programming language to make pipelines, Python in this case.

I had to install pandas package first:

    pip3 install pandas 

<img src="https://github.com/victorjulyin/DE-101/blob/main/Apache%20Airflow/M1_cron_and_base_info/pics/M1_2.png" width=50% height=50%>

Then I used [this script](ССЫЛЬ НА ФАЙЛ КОТОРЫЙ В ПАПКЕ) to send go through that pipeline (I didn't write it).

<img src="https://github.com/victorjulyin/DE-101/blob/main/Apache%20Airflow/M1_cron_and_base_info/pics/m1_3.png" width=50% height=50%>

#### I had a problem

When I tried to start the command via Terminal I received this error:

    urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:997)>


Then I found this file => clicked on it => the problem was solved:

    /Applications/Python 3.10/Install Certificates.command



### CRON setup

<img src="https://github.com/victorjulyin/DE-101/blob/main/Apache%20Airflow/M1_cron_and_base_info/pics/m1_4.png" width=50% height=50%>


To edit or create a crontab file:

    $ export EDITOR=nano
    $ crontab -e



I'll use this script:

    $ 0 10 * * * python3 *full_path*


To quit and save push **ctrl + X** => **Y**.

Finally:

    0 10 * * * /usr/local/bin/python3 "/Users/a1/Documents/GitHub/DE-101/Apache Airflow/M1 ETL introduction - Write the pipeline/try_m1.py"

<img src="https://github.com/victorjulyin/DE-101/blob/main/Apache%20Airflow/M1_cron_and_base_info/pics/m1_5.png" width=50% height=50%>

#### Some Bash notes

    # delete all symbols in a row
    $ ctrl + K 

    # go to the row end 
    $ ctrl + e

    # go to the row start
    $ ctrl + a

### Everything works, but there are some problems

  * We can't see at what step our script broke
  * Is idempotence saved?
  * How to inform us that script broke down?
  * All steps in sequence

These are problems that are solved with tools such as Airflow.

## Theory

### DAG

Directed Acyclic Graph:
  * Doesn't have cycles
  * Every node has an direction
  * Parallel steps possibility
  * Finiteness of the system

<img src="https://github.com/victorjulyin/DE-101/blob/main/Apache%20Airflow/M1_cron_and_base_info/pics/m1_6.png" width=50% height=50%>
<img src="https://github.com/victorjulyin/DE-101/blob/main/Apache%20Airflow/M1_cron_and_base_info/pics/m1_7.png" width=50% height=50%>

### Idempotency

This is a property of a system or procedure that means that its results are independent of external factors and do not change when called again with the same input.

For example, this function returns the figure square:

  def square(x):
    return x * x

If we'll call square(5) now and one month later, the result will be the same. This is idempotency.
In the Data case - it is important to not duplicate Data.


## Python pipeline creation

<img src="https://github.com/victorjulyin/DE-101/blob/main/Apache%20Airflow/M1_cron_and_base_info/pics/m1_8.png" width=50% height=50%>
This is what we need to do.

  # import necessary libraries
  import sqlite3 as sl
  import pandas as pd


  # sqlite DB creation
  conn = sl.connect('my-test.db')
  cursor = conn.cursor()

  # Function for currencies parsing 
  def extract_currency(date, base='EUR', symbols='USD', format='csv'):
    url = f'https://api.exchangerate.host/timeseries?start_date={date}&end_date={date}&base={base}&symbols={symbols}&format={format}'
    
    response = pd.read_csv(url)
    return response

  # Function for a .csv file parsing
  def extract_data(date):
    url = f'https://raw.githubusercontent.com/dm-novikov/stepik_airflow_course/main/data_new/{date}.csv'
    df = pd.read_csv(url, squeeze=True)
    return df


  # Function that loads data to DB
  def insert_to_db(data, table_name, conn=conn, if_exists = 'replace'):
    data.to_sql(table_name, conn, if_exists=if_exists, index = False)


  # Function that executes SQL-queries
  def sql_query(sql, conn=conn, cursor=cursor):
    cursor.execute(sql)
    conn.commit()
    d = cursor.fetchall()
    return d


  # Main

  dates_list = [f'2021-01-0{x}' for x in range(1,5)]

  def main(date, conn=conn):

  # Download currencies and data from Githab 
  currency = extract_currency(date)
  data = extract_data(date)
 
  # Create the tables

  sql_query('CREATE TABLE IF NOT EXISTS currency (currency text, value float, date date)') 
  sql_query('CREATE TABLE IF NOT EXISTS data (date date, code text, rate float, base text, start_date date, end_date date)') 
  sql_query('CREATE TABLE IF NOT EXISTS join_data (val_eur float, val_usd, date date)') 

  # Insert the data to DB
  insert_to_db(currency, 'currency')
  insert_to_db(data, 'data')

  
  # join_data table filling
  sql_query('''INSERT INTO join_data
               SELECT value, round(value * CAST(replace(rate, ',', '.') as float), 2), currency.date
               FROM currency INNER JOIN data
               ON currency = base AND currency.date = data.date
            ''')

  
  # Clean temporary tables
  sql_query('DROP TABLE IF EXISTS currency')
  sql_query('DROP TABLE IF EXISTS data')

  
  # Fetch data from join_data table for a specific day
  report = sql_query(f"SELECT * FROM join_data where date = '{date}'")

  # Start "main" function
  for date in dates_list:
    main(date)
