# ITMD 521 Spring 2018

## Week 13 Spark Assignment

### Objectives 

* Understand how to deploy a local Spark Cluster
* Understand the differences and similarities between MapReduce and Spark
* Understand the SparkContext concept 
* Understand how to use PySpark and Spark-Shell to process big data into meaningful results

### Outcomes 

At the conclusion of this lab you will have a basic understanding of the terminology and concepts of Spark and its advantages and disadvantages over the MR platform


### Part I

In chapter 19 of the textbook, you are to install the Spark open-source cluster-computing framework on your local Hadoop Cluster (Vagrant Box). 

Using these datasets, as a basis using your python script from earlier in the semester, create a hybrid data set containing only, **longitude**, **air temperature**, and **air temperature quality code**, seperated by a **TAB**, **/t**

* A-E 1997.txt 1997.txt.xz
* F-R 1950.txt 1950.txt.xz
* S-Z 1985.txt 1985.txt.xz

Provide a spark script (in either python or scala) that will find the max temperature per 10 degree of longitude (agregate the ranges so 20.000 to 29.999, 30.000 to 39.999, for example)


### Deliverable 1

Submit your Github repo URL to blackboard by 11:59 pm April 19th.

In your Week-13 folder include all scripts and program instructions needed to retrieve and reproduce your results.  Upload your part-r-0000 file (results) as well)  Write and instruction/assumptions needed in the Assumption section below.

![Maximum_Temperature_with_Longitude](https://github.com/illinoistech-itm/ssaxena12/blob/master/ITMD-521/Week-13/Images/Week-13.PNG)

### Assumptions 1

Initially Spark is installed on the vagrant followed by unzipping the respective tar.

A new python file named part1 is made which consist the python code to extract the data into a new text file named outputbyshivank.txt as a new hybrid dataset.
A second python script named part2 is made which runs the mapper and reducer and gives out the output of maximum temperature based on the longitudinal directions. The output file generated in named as MaximumTemperature.txt.

Finally a cat command it implemented to display the output.
