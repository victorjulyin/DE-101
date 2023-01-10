## A list of the exercises 

  * [Interesting things that I got](#interesting-things-that-i-got)

  * [Find products that are not in stock](#find-products-that-are-not-in-stock) (file)
  * [Create a list of buyers](#create-a-list-of-buyers) 
  * [Create a list of suggested products using Database Join](#create-a-list-of-suggested-products-using-database-join)
  * [Create a list of buyers (using DB Join)](#create-a-list-of-buyers-using-db-join)
  * [Update "region" field](#update-region-field-after-tutorial)
  * [Update manufacturers table](#update-manufacturers-table)




## Interesting things that I got

  * [Group By](#group-by) - almost the same thing as in SQL
  * [Database Lookup](#database-lookup) - use it, when we need to add some data from another DB / Table (almost like join)
  * [Database Join](#database-join) - you can join tables from DW with tables from any other source (excel, txt, etc)
  * [Combination lookup/update](#combination-lookupupdate) - use it, when we want to update DB time to time. It will help to find different rows and add it with key (SCD Type I)
  * [Stream Lookup](#stream-lookup) - use it, when you want to connect data from different sources. 
  * [Dimension Lookup/Update](#dimension-lookupupdate) - use it, when you want to save the history changes (SCD Type II)
  * Dimension - A dimension table contains descriptions about a particular entity or category of your business. Dimensions are one of the basic blocks of a data warehouse or a datamart. A dimension has the purpose of grouping, filtering, and describing data.
  * Slowly Changing Dimension (SCD) - A dimension where changes may occur from time to time (it has three types)
    * I type - you don't keep the history of changes
    * II type - you keep the whole history of changes

Videos that hepled me to understand these things:
[Combination lookup/update](https://www.youtube.com/watch?v=J_DyORTSklY)
[Stream lookup](https://www.youtube.com/watch?v=ktzB2AzX_-s)



### Group By
<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/Module4/4.5%20Pentaho%20Data%20Integration%20Beginner's%20Guide%20-%20Chapter%209%20Exercises/pics/4.5_2.png"></p>


### Database Lookup
<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/Module4/4.5%20Pentaho%20Data%20Integration%20Beginner's%20Guide%20-%20Chapter%209%20Exercises/pics/4.5_3.png"></p>


### Database Join
<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/Module4/4.5%20Pentaho%20Data%20Integration%20Beginner's%20Guide%20-%20Chapter%209%20Exercises/pics/4.5_6.png"></p>

### Combination Lookup/Update
<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/Module4/4.5%20Pentaho%20Data%20Integration%20Beginner's%20Guide%20-%20Chapter%209%20Exercises/pics/4.5_8.png"></p>

### Stream Lookup
<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/Module4/4.5%20Pentaho%20Data%20Integration%20Beginner's%20Guide%20-%20Chapter%209%20Exercises/pics/4.5_9.png"></p>

### Dimension Lookup/Update
<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/Module4/4.5%20Pentaho%20Data%20Integration%20Beginner's%20Guide%20-%20Chapter%209%20Exercises/pics/4.5_13.png"></p>

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/Module4/4.5%20Pentaho%20Data%20Integration%20Beginner's%20Guide%20-%20Chapter%209%20Exercises/pics/4.5_14.png"></p>








## The exercises

### Find products that are not in stock
<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/Module4/4.5%20Pentaho%20Data%20Integration%20Beginner's%20Guide%20-%20Chapter%209%20Exercises/pics/4.5_1.png"></p>


### Create a list of buyers
<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/Module4/4.5%20Pentaho%20Data%20Integration%20Beginner's%20Guide%20-%20Chapter%209%20Exercises/pics/4.5_4.png"></p>


### Create a list of suggested products using Database Join 
<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/Module4/4.5%20Pentaho%20Data%20Integration%20Beginner's%20Guide%20-%20Chapter%209%20Exercises/pics/4.5_5.png"></p>


### Create a list of buyers (using DB Join)
<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/Module4/4.5%20Pentaho%20Data%20Integration%20Beginner's%20Guide%20-%20Chapter%209%20Exercises/pics/4.5_7.png"></p>

### Update "region" field (after tutorial)
#### Tutorial
<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/Module4/4.5%20Pentaho%20Data%20Integration%20Beginner's%20Guide%20-%20Chapter%209%20Exercises/pics/4.5_11.png"></p>

#### Exercise
<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/Module4/4.5%20Pentaho%20Data%20Integration%20Beginner's%20Guide%20-%20Chapter%209%20Exercises/pics/4.5_10.png"></p>

### Update manufacturers table
<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/Module4/4.5%20Pentaho%20Data%20Integration%20Beginner's%20Guide%20-%20Chapter%209%20Exercises/pics/4.5_12.png"></p>

### Load the Regions dimension as a Type II SCD
<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/Module4/4.5%20Pentaho%20Data%20Integration%20Beginner's%20Guide%20-%20Chapter%209%20Exercises/pics/4.5_15.png"></p>

