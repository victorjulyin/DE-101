## A list of the exercises 

  * [Interesting things that I got](#interesting-things-that-i-got)

  * [Find products that are not in stock](#find-products-that-are-not-in-stock) ([file](https://github.com/victorjulyin/DE-101/blob/main/Module4/4.5%20Pentaho%20Data%20Integration%20Beginner's%20Guide%20-%20Chapter%209%20Exercises/files/1%20Have%20a%20go%20hero%20–%20preparing%20the%20delivery%20of%20the%20products%20(p290).ktr))
  * [Create a list of buyers](#create-a-list-of-buyers) ([file](https://github.com/victorjulyin/DE-101/blob/main/Module4/4.5%20Pentaho%20Data%20Integration%20Beginner's%20Guide%20-%20Chapter%209%20Exercises/files/2%20Have%20a%20go%20hero%20–%20refining%20the%20transformation(p291).ktr))
  * [Create a list of suggested products using Database Join](#create-a-list-of-suggested-products-using-database-join) ([file](https://github.com/victorjulyin/DE-101/blob/main/Module4/4.5%20Pentaho%20Data%20Integration%20Beginner's%20Guide%20-%20Chapter%209%20Exercises/files/3%20Time%20for%20action%20–%20using%20a%20join%20step%20to%20create%20a%20list%20of%20suggested%20products%20(p293).ktr))
  * [Create a list of buyers (using DB Join)](#create-a-list-of-buyers-using-db-join) ([file](https://github.com/victorjulyin/DE-101/blob/main/Module4/4.5%20Pentaho%20Data%20Integration%20Beginner's%20Guide%20-%20Chapter%209%20Exercises/files/4%20Have%20a%20go%20hero%20–%20rebuilding%20the%20list%20of%20customers.ktr))
  * [Update "region" field (SCD I)](#update-region-field-after-tutorial) ([file](https://github.com/victorjulyin/DE-101/blob/main/Module4/4.5%20Pentaho%20Data%20Integration%20Beginner's%20Guide%20-%20Chapter%209%20Exercises/files/8%20Time%20for%20action%20–%20keeping%20a%20history%20of%20changes%20in%20products%20by%20using%20the%20Dimension%20lookup:update%20step.ktr))
  * [Update manufacturers table](#update-manufacturers-table) ([file](https://github.com/victorjulyin/DE-101/blob/main/Module4/4.5%20Pentaho%20Data%20Integration%20Beginner's%20Guide%20-%20Chapter%209%20Exercises/files/7%20Have%20a%20go%20hero%20update%20manufacturers.ktr))
  * [Load the Regions dimension as a Type II SCD](#load-the-regions-dimension-as-a-type-ii-scd) ([file](https://github.com/victorjulyin/DE-101/blob/main/Module4/4.5%20Pentaho%20Data%20Integration%20Beginner's%20Guide%20-%20Chapter%209%20Exercises/files/10%20Have%20a%20go%20hero%20–%20loading%20the%20Regions%20dimension%20as%20a%20Type%20II%20SCD.ktr))
  * [Final: Create a mini-demension with with puzzles attributes]()




## Interesting things that I got

  * [Group By](#group-by) - almost the same thing as in SQL
  * [Database Lookup](#database-lookup) - use it, when we need to add some data from another DB / Table (almost like join)
  * [Database Join](#database-join) - you can join tables from DW with tables from any other source (excel, txt, etc)
  * [Combination lookup/update](#combination-lookupupdate) - use it, when we want to update DB time to time. It will help to find different rows and add it with key (SCD Type I)
  * [Stream Lookup](#stream-lookup) - use it, when you want to connect data from different sources. 
  * [Dimension Lookup/Update](#dimension-lookupupdate) - use it, when you want to save the history changes (SCD Type II)
  * Dimension - A dimension table contains descriptions about a particular entity or category of your business. Dimensions are one of the basic blocks of a data warehouse or a datamart. A dimension has the purpose of grouping, filtering, and describing data.
  * Slowly Changing Dimension (SCD) - A dimension where changes may occur from time to time (it has three types)
    * I(0) type - you don't keep the history of changes
    * II type - you keep the whole history of changes
    * III type - you keep only current and previous value 

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

### Final: Create a mini-demension with with puzzles attributes
<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/Module4/4.5%20Pentaho%20Data%20Integration%20Beginner's%20Guide%20-%20Chapter%209%20Exercises/pics/4.5_16.png"></p>

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/Module4/4.5%20Pentaho%20Data%20Integration%20Beginner's%20Guide%20-%20Chapter%209%20Exercises/pics/4.5_17.png"></p>

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/Module4/4.5%20Pentaho%20Data%20Integration%20Beginner's%20Guide%20-%20Chapter%209%20Exercises/pics/4.5_18.png"></p>
