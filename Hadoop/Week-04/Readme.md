# ITMD 521 Spring 2018

## Week 4 assignment

Clone this repo to your system, add this file to a folder named Week-04 (mind the spelling) under ITMD-521 in your own private github repo

### Part I

* Insert the assigned datasets below into your local hadoop cluster 
  + A-E 1997.txt [1997.txt.xz](https://drive.google.com/open?id=0Bys2c__9q7eBNzhMNXdUSFpNYlk)
  + F-R 1950.txt [1950.txt.xz](https://drive.google.com/open?id=0Bys2c__9q7eBQVJnbXFMSkstMTQ)
  + S-Z 1985.txt [1985.txt.xz](https://drive.google.com/open?id=0Bys2c__9q7eBUUN4TkllRXFxYTg)
  + Note that the files are compressed with xzip - you will need to use the vagrant shared file options to get them into your vagrant box - see Week 4 Tuesday video 
* Insert the data into this directory structure /user/$USER/ncdc/19XX/  (with XX being your year)
* Compile the source code in chapter-02 of the text book sample code into a single jar file named: ```mt.jar```
  + Place all your scripts (but not the datafile!) into the Week-04 github folder
* Run the MaxTemperature class against your dataset
* Display the content of the part-r-00000 and capture that in a screenshot to be displayed below

### Part II

* In your Vagrant box, install mysql-server and give it the password: **itmd521**
* Install and configure the proper mysql-Java connector - [mysql/J connector](https://dev.mysql.com/downloads/connector/j/)
* Write a script in Python to parse the dataset given you (using schemea in Chapter 02) and insert this data into a database named: **521** and a table named: **records**
  + Assume that the dataset.txt file is in the same directory as the script being executed
* Write a Java Application that will perform the same funtionality as the MapReduce program to find the Max Temperature in SQL.
* Provide any instructions or additional dependencies needed at the bottom of this document
  + We will run your code to see if the results are as delvivered.
  + Place all your scripts (but not the datafile!) into the Week-04 github folder
* take a screenshot of the output 

 Assume all work and code will be executed on the Vagrant Box

### Deliverable 1

![Successful installation of Hadoop version](https://github.com/illinoistech-itm/ssaxena12/blob/master/ITMD-521/Week-04/Images/1(a).png)

### Devliverable 2

![Successful installation of Hadoop version](https://github.com/illinoistech-itm/ssaxena12/blob/master/ITMD-521/Week-04/Images/2..PNG)

### Additional Notes
1st output has been clicked on powershell6.0.0 whereas the output of 2nd Step has been clicked in windows powershell as there were unknwon application errors occuring while executing certain commands in powershell6.0.0
