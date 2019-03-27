# ITMD 521 Spring 2018

## Week 11 assignment

### Objectives 

* Install and configure industry standard VPN software 
* Configure and connect to industry standard VPN 
* Configure hadoop 2.6.5 installation to connect to a remote Hadoop cluster 
* Understand and analyze the effect of combiners on large MapReduce jobs

### Outcomes 

At the conclusion of this lab you will understand the reasons behind and be able to conenct to a remote network via a VPN.  You will have configured your Hadoop installation to connect to a remote cluster and will have run large scale jobs and analyzed the effect of Reducer classes upon the run time of the job.


### Part I

Assuming that you have succesfully installed, configured, and connected to the remote network via the VPN provided, you need to clone all of the configuration files (see note below) and properly configure you hadoop installation to connect to the remote Hadoop Cluster

Execute this command from your itmd521-cluster vagrant box ```hadoop fs -ls /user/controller/ncdc/1990/``` and take a screenshot of the output.  Place that image in **Deliverable 1** below.

### Deliverable for Part 1
![itmd521_cluster](https://github.com/illinoistech-itm/ssaxena12/blob/master/ITMD-521/Week-11/Images/Part%20-1.PNG)

### Part II 

Compile the MaxTemperature sample code from the hadoop-book chapter 02.  Place the code into a jar file mt.jar (you may already have this step done, which in that case you can reuse mt.jar).  Run the command ```hadoop jar mt.jar MaxTemperature /user/controller/ncdc/YEAROFYOURBIRTH/YEAROFYOURBIRTH.txt``` and ```hadoop jar mt.jar MaxTemperatureWithCombiner /user/controller/ncdc/YEAROFYOURBIRTH/YEAROFYOURBIRTH.txt```

Repeat the above with this command:  ```hadoop jar mt.jar MaxTemperature /user/controller/ncdc/60-70/60-70.txt``` and ```hadoop jar mt.jar MaxTemperatureWithCombiner /user/controller/ncdc/60-70/60-70.txt```

Run each of these three times, capture a screenshot(s) of only these jobs (not others) include them in **Deliverable 2**   This will give you a total of 12 jobs

Note the execution time and graph all of the occurances (six job runs vs time to execute).  Place an image of that graph in ### 

### Deliverable for Part 2

 Outputs of Birth year without Combiner
![Birth year without Combier - 1](https://github.com/illinoistech-itm/ssaxena12/blob/master/ITMD-521/Week-11/Images/1%20-%20a.PNG)

![Birth year without Combier - 2](https://github.com/illinoistech-itm/ssaxena12/blob/master/ITMD-521/Week-11/Images/1%20-%20b.PNG)

![Birth year without Combier - 3](https://github.com/illinoistech-itm/ssaxena12/blob/master/ITMD-521/Week-11/Images/1%20-%20c.PNG)

 Outputs of Birth year with Combiner

![Birth year with Combier - 1](https://github.com/illinoistech-itm/ssaxena12/blob/master/ITMD-521/Week-11/Images/2%20-%20a.PNG)

![Birth year with Combier - 2](https://github.com/illinoistech-itm/ssaxena12/blob/master/ITMD-521/Week-11/Images/2%20-%20b.PNG)

![Birth year with Combier - 3](https://github.com/illinoistech-itm/ssaxena12/blob/master/ITMD-521/Week-11/Images/2%20-%20c.PNG)

 Outputs of Decade without Combiner

![Decade without Combier - 1](https://github.com/illinoistech-itm/ssaxena12/blob/master/ITMD-521/Week-11/Images/3%20-%20a.PNG)

![Decade without Combier - 2](https://github.com/illinoistech-itm/ssaxena12/blob/master/ITMD-521/Week-11/Images/3%20-%20b.PNG)

![Decade without Combier - 3](https://github.com/illinoistech-itm/ssaxena12/blob/master/ITMD-521/Week-11/Images/3%20-%20c.PNG)

 Outputs of Decade with Combiner

![Decade with Combier - 1](https://github.com/illinoistech-itm/ssaxena12/blob/master/ITMD-521/Week-11/Images/4%20-%20a.PNG)

![Decade with Combier - 2](https://github.com/illinoistech-itm/ssaxena12/blob/master/ITMD-521/Week-11/Images/4%20-%20b.PNG)

![Decade with Combier - 3](https://github.com/illinoistech-itm/ssaxena12/blob/master/ITMD-521/Week-11/Images/4%20-%20c.PNG)

 GRAPHS
 
![Birth Year with and without combiner](https://github.com/illinoistech-itm/ssaxena12/blob/master/ITMD-521/Week-11/Images/Birth%20Year%20with%20and%20without%20combiner.PNG)

![Decade with and without combiner](https://github.com/illinoistech-itm/ssaxena12/blob/master/ITMD-521/Week-11/Images/Decade%20with%20and%20without%20combiner.PNG)


### Part III

Using the textbook and the previous chapters, explain the effect of the reducer upon the outcomes of the job execution time from Part II in technical detail (It is faster or slower is not an acceptable answer).  Cite page sources from the book explaining how you arrived at your answer.
### Deliverable for Part 3

Clusters run MapReduce jobs with a limitation of bandwidths upon them which restricts the data transfer between mapper and reducer. After the job submission to the mapper, user selects the appropriate combiner function for it which helps in data optimization. It is also independent of the number of times a reducer is called for execution and o it produces the same output every time. Both mapper and reducers are dependent upon each other which saves a lot of time of shuffling of data among them.

It can be observed from the date of birth set which is 1993, the average execution time 61 seconds without combiner and 46 seconds with combiner. The execution time with combiner has reduced drastically. Similarly, for 60-70 dataset the average time without combiner is 394 seconds and 277 seconds. It happens because the combiner allocates the data meaningfully which makes data processing easier for the Reducer. The combiner’s output is sent over the network using the same key to the reducer’s phase so that it makes easy for Hadoop combiner to reduce network congestion which in turn increases the efficiency of the network which can also be seen in my results.


## Setup Remote Hadoop Cluster Notes

Copy all *.xml and .sh files into your ```~/hadoop-2.6.5/etc/hadoop``` directory overwritting the defaults 

Copy the hosts file content into your ```/etc/hosts file``` -- note ```/etc/hosts``` is owned by root so you need to use ```sudo```
