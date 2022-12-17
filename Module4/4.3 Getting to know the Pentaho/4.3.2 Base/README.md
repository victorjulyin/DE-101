# Job creation

## The plan

* [Download superstore-sample.xls (job1)](#download-superstore-samplexls-by-http-and-shell)
* [Merge three tables into one (Transformation1)](#merge-three-tables-into-one)
* [Split data into different formats (Transformation2)](#split-data-into-different-formats)
** Products data - JSON
** Returns data - XML
** Orders by regions:
*** CENTRAL - XLS
*** WEST - "California", "Arizona", "Washington" and "Others" - csv
*** SOUTH - csv (zip)
*** EAST - text file .dat
* [Add "marks" for more realism (Transformation3)](#add-marks)
** WEST - different country names (US, USA, United States), extra symbols in "city" field
** EAST - add typos in city names (difficult to predict for manual correction)
** SOUTH - duplicate orders



## Download superstore-sample.xls by HTTP and shell

### All jobs start with "play". And add "HTTP"

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/Module4/4.3%20Getting to know the Pentaho/4.3.2%20Base/pics/job1.png"></p>

### HTTP configs

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/Module4/4.3%20Getting to know the Pentaho/4.3.2%20Base/pics/job2.png"></p>

### Add shell

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/Module4/4.3%20Getting to know the Pentaho/4.3.2%20Base/pics/job3.png"></p>

### Shell configs

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/Module4/4.3%20Getting to know the Pentaho/4.3.2%20Base/pics/job4.png"></p>

### Shell script

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/Module4/4.3%20Getting to know the Pentaho/4.3.2%20Base/pics/job5.png"></p>

### Connect everything 

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/Module4/4.3%20Getting to know the Pentaho/4.3.2%20Base/pics/job6.png"></p>

### Result of the launching

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/Module4/4.3%20Getting to know the Pentaho/4.3.2%20Base/pics/job7.png"></p>


## Merge three tables into one

### Nothing special, but it is important to sort data before merge

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/Module4/4.3%20Getting to know the Pentaho/4.3.2%20Base/pics/Transformation1.png"></p>


## Split data into different formats

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/Module4/4.3%20Getting to know the Pentaho/4.3.2%20Base/pics/Transformation2.png"></p>



## Add marks