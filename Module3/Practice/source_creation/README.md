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
(sqldbm1 screen)
SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! 

### The Queries / creation source DB

LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! 
Here is [the file](ASDASDASDASDASDASDASDASD) with all of the queries to create the DB.

Querie sample:

    CREATE TABLE calendar
    (
    calendar_id    int NOT NULL,
    listing_id     int NOT NULL,
    "date"           date NOT NULL,
    available      varchar(10) NOT NULL,
    price          int NOT NULL,
    adjusted_price int NOT NULL,
    minimum_nights int NOT NULL,
    maximum_nights int NOT NULL,
    CONSTRAINT PK_1 PRIMARY KEY ( calendar_id )
    );


### The Queries / filling source DB

LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! LINK! 
Here is [the file](ASDASDASDASDASDASDASDASD) with all of the queries to fill the DB.

Querie sample:




### Created tables in DBeaver
(DBeaver1 screen)
SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! SCREEN! 


### Filled tables in DBeaver



Не получается импортировать всю инфу из фалов csv
из-за того, что я сделал первые поля id
Надо их удалить все, сделать заново все sql-запросы
и уже тогда импортировать

COPY calendar 
FROM '/Users/a1/Downloads/archive/calendar.csv' 
DELIMITER ',' 
CSV HEADER;





