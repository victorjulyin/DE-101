## What do we have?

This is our [source files](https://www.kaggle.com/datasets/labdmitriy/airbnb?resource=download)

* calendar - availability of the flat during the year
* listings - detailed information about each offers
* listings_summarry - summary info about each object (less coloumns)
* neighbourhoods - district list
* neighbourhoods.geojson - geo shape of a district 
* reviews - review list by each object
* reviews_summary - summary info by reviews 

## Source DataBase creation

I used "SQLdbm" service to create SQL-queries for the DB.

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/Module3/Practice/source_creation/sqldbm1.png"></p>


### The Queries / creation source DB

Here is [the file](https://github.com/victorjulyin/DE-101/blob/main/Module3/Practice/source_creation/sql_create_db.txt) with all of the queries to create the DB.

Querie sample:

    CREATE TABLE calendar
    (
    listing_id     int NOT NULL,
    "date"           date NOT NULL,
    available      varchar(10) NOT NULL,
    price          int NOT NULL,
    adjusted_price int NOT NULL,
    minimum_nights int NOT NULL,
    maximum_nights int NOT NULL,
    );


### Created tables in DBeaver

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/Module3/Practice/source_creation/dbeaver1.png"></p>





### The Queries / filling source DB

WRONG WRONG WRONG WRONG WRONG WRONG WRONG WRONG WRONG WRONG WRONG WRONG
WRONG WRONG WRONG WRONG WRONG WRONG WRONG WRONG WRONG WRONG WRONG WRONG
WRONG WRONG WRONG WRONG WRONG WRONG WRONG WRONG WRONG WRONG WRONG WRONG
WRONG WRONG WRONG WRONG WRONG WRONG WRONG WRONG WRONG WRONG WRONG WRONG
Here is [the file](https://github.com/victorjulyin/DE-101/blob/main/Module3/Practice/source_creation/sql_fill_db.txt) with all of the queries to fill the DB.

Querie sample:

    COPY calendar 
    FROM '/Users/a1/Downloads/archive/calendar.csv' 
    DELIMITER ',' 
    CSV HEADER;




### Filled tables in DBeaver
<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/Module3/Practice/source_creation/dbeaver2.png"></p>



