## I created a few transformations

  * [About functions](#about-functions)
  * [Tutorial 1](#data-creation-and-calculations): Data creation => calculations => expression
  * [Tutorial 2](#data-creation-and-filter): Data creation => filter => calculations
  * [Tutorial 3](#from-source-to-postgres): Transporting Data from the source to a Postgres DB
  * [Tutorial 4](#dw-creation): DW creation
  * [Tutorial 5](#dimension-tables-creation): Dimension tables creation
  * [Sales_fact table](#sales_fact-table-creation): Table creation
  * [Final job](#final-job)
 
Source files:
  * [tutorial1.ktr](https://github.com/victorjulyin/DE-101/blob/main/Module4/4.4%20Continuing%20with%20PentahoDI/tutorial1.ktr)
  * [tutorial2.ktr](https://github.com/victorjulyin/DE-101/blob/main/Module4/4.4%20Continuing%20with%20PentahoDI/tutorial2.ktr)
  * [tutorial3.ktr](https://github.com/victorjulyin/DE-101/blob/main/Module4/4.4%20Continuing%20with%20PentahoDI/tutorial3.ktr)
  * [tutorial4.ktr](https://github.com/victorjulyin/DE-101/blob/main/Module4/4.4%20Continuing%20with%20PentahoDI/tutorial4.ktr)
  * [tutorial5.ktr](https://github.com/victorjulyin/DE-101/blob/main/Module4/4.4%20Continuing%20with%20PentahoDI/tutorial5.ktr)
  * [sales_fact.ktr](https://github.com/victorjulyin/DE-101/blob/main/Module4/4.4%20Continuing%20with%20PentahoDI/sales_fact.ktr)
  * [pentaho_job.ktr](https://github.com/victorjulyin/DE-101/blob/main/Module4/4.4%20Continuing%20with%20PentahoDI/pentaho_job.ktr)


------------------------------
### About functions

  * Generate Rows - fast row generating (with similar value)
  * Dummy - do nothing
  * Data Grid - easy table creation
  * Calculator - some calculations
  * Number Range - like CASE in SQL (if ... then ... inside a table)
  * User Defined Java Expression - custom expression on Java
  * Select Values - ...
  * Write to log - ...
  * Table Input/Output - we can connect to Postgres (for example) and load/download Data
  * Unique rows - distinct
  * Add sequence - add custom key

------------------------------
### Data creation and calculations

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/Module4/4.4%20Continuing with PentahoDI/pics/transf1.png"></p>

------------------------------

### Data creation and filter

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/Module4/4.4%20Continuing with PentahoDI/pics/transf2.png"></p>

------------------------------

### From source to Postgres

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/Module4/4.4%20Continuing with PentahoDI/pics/transf3.png"></p>

------------------------------

### DW creation

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/Module4/4.4%20Continuing with PentahoDI/pics/transf4.png"></p>

------------------------------

### Dimension tables creation

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/Module4/4.4%20Continuing with PentahoDI/pics/transf5.png"></p>

------------------------------

### sales_fact table creation

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/Module4/4.4%20Continuing with PentahoDI/pics/sales_fact_transf.png"></p>

------------------------------

### Final Job

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/Module4/4.4%20Continuing with PentahoDI/pics/final_job.png"></p>

------------------------------