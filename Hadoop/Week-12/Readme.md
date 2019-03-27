# ITMD 521 Spring 2018

## Week 12 assignment

### Objectives 

* Understand the effect (positive and negative) of using multiple reducers on an MR job 
* Understand the effect of using Intermediate Compression on an MR job
* Understand the benefit of using custom counters in the output of an MR job 
* Understand how to modify and change the jobname of an MR job

### Outcomes 

At the conclusion of this lab you will have run through a matrix of MR jobs with various optimizations relating to the number of reducers, use of intermediate compression, and the use of a combiner class.  In addition you will modify the sample MR code to include try/catch logic and a custom counter bad and invalid records.


### Part I

Using the single year of your birth, modify the sample MaxTemperature class to include a custom counter to count all bad (malformed) records and count all invalid ranged records (for instance anything greater than 50.0 celsius).  Disply the output of these two counters at the end of your MR output and take a screenshot of the output.  Place that image in **Deliverable 1** below. Submit your modified code into week 12 Github folder as well.

### Deliverable 1
#### Screenshot (Powershell)
![Malformed/Invalid Records_powershell](https://github.com/illinoistech-itm/ssaxena12/blob/master/ITMD-521/Week-12/Images/Part%201%20Malformed%20Records(PWS).PNG)

#### Screenshot (history server)
![Malformed/Invalid Records_historyserver](https://github.com/illinoistech-itm/ssaxena12/blob/master/ITMD-521/Week-12/Images/Part%201%20Malformed%20Records(2).PNG)

### Part II - Reducers

Using the dataset for the year you were born, run the MaxTemperature and MaxTempertature jobs each using 1, and then 2 reducers; four jobs total.

Capture a screenshot(s) of only these jobs (not others) include them in **Deliverable 2**   

Note the execution time and graph all of the occurances.  Place an image of that graph in **Deliverable 2**

Using the textbook and the previous chapters, explain the effect of the reducer upon the outcomes of the job execution time from Part II in technical detail (It is faster or slower is not an acceptable answer).  **Cite page sources from the book explaining how you arrived at your answer.**

### Deliverable 2
##### With 1 Reducer
![Maxtemp_with_1_Reducer](https://github.com/illinoistech-itm/ssaxena12/blob/master/ITMD-521/Week-12/Images/Part%202%20-%201%20Reducer.PNG)

![Maxtemp_with_1_Reducer_Combiner](https://github.com/illinoistech-itm/ssaxena12/blob/master/ITMD-521/Week-12/Images/Part%202%20-%201%20with%20combiner.PNG)


##### With 2 Reducer
![Maxtemp_with_2_Reducer](https://github.com/illinoistech-itm/ssaxena12/blob/master/ITMD-521/Week-12/Images/Part%202%20-%202%20Reducer.PNG)

![Maxtemp_with_2_Reducer_Combiner](https://github.com/illinoistech-itm/ssaxena12/blob/master/ITMD-521/Week-12/Images/Part%202%20-%202%20with%20combiner.PNG)

#### Graph

![Graph Interpretation](https://github.com/illinoistech-itm/ssaxena12/blob/master/ITMD-521/Week-12/Images/Graph%20Part%20-%202.PNG)

#### Description

In practical scenario, a job in run on executed by multiple reducer and not just 1, as it takes a lot of time for the process. Therefore it is not practically possible to execute the reduction phase of any job by just using a single reducer. Hence chosing the number of reducers is the crucial part of MR job which helps in optimizing the time. The less number of reducers, the more load on the nodes which at times can cause node failure with no chance of recovery.The problem also arises when there are excess number of reducersmore than what is require for job execution causing shuffle crossbar in which multiple files are created which inturn impacts the performance of the namenode.

It can be understood from the graph that the Max temperature with 1 reducer consumes less time for job execution than Max temperature with 2 reducers. As the number of Reducers increases, the data transfer and processing time among reducers and across the network also increases which results in more final job execution time. The combiner helps in cutting down the execution time by organizing the shuffle of data between mapper and reducer thus optimizing the data as a local reducer.

#### References
https://stackoverflow.com/questions/39541718/why-increasing-the-number-of-reducers-increases-the-time-for-running-reduce-phas

### Part III - Reducers Large

Using the linux command [md5](https://en.wikipedia.org/wiki/MD5 "md5") to take a hash of your Hawk ID: ```echo "hajek" | md5sum```.  Take a screenshot of this output and include it in **Deliverable 3**. 

Based on the output string use two datasets mentioned below:

1) If first character is even number: use 50.txt
1) If first character is odd number use: 60.txt
1) If first character is a letter use: 60-70.txt
1) In addition to the above everyone needs to use 60-90.txt as well.

* Enable **intermediate compression**, Page 118 of epub, for all of your MR jobs in this section.
* Compile your code to contain the job.setName("Initials here and a description") value
* Run 8 jobs on each dataset (8x2=16 total), 
* Run your first dataset assigned above: MaxTemperature
    + with 1, 2, 4, 8 reducers
* Run your first dataset assigned above: MaxTemperatureWithCombiner
    + with 1, 2, 4, 8 reducers
*  * Run your second dataset assigned above: MaxTemperature
    + with 1, 2, 4, 8 reducers
* Run your second dataset assigned above: MaxTemperatureWithCombiner
    + with 1, 2, 4, 8 reducers  

Capture a screenshot(s) of only these jobs (not others) include them in **Deliverable 3**   

Note the execution time and graph all of the occurances.  Place an image of those graphs in **Deliverable 3**

Using the textbook and the previous chapters, explain the effect of the reducer upon the outcomes of the job execution time from Part II in technical detail (It is faster or slower is not an acceptable answer).  **Cite page sources from the book explaining how you arrived at your answer.**  

### Deliverable 3
#### Screenshot of echo "ssaxena12" | md5sum
![Echo](https://github.com/illinoistech-itm/ssaxena12/blob/master/ITMD-521/Week-12/Images/1.%20Part%203%20Echo.PNG)

#### Jobs according to DataSet letter as first character 60-70.txt
##### Without Combiner
![Dataset60-70_Reducer1](https://github.com/illinoistech-itm/ssaxena12/blob/master/ITMD-521/Week-12/Images/Part%203%20a%20(1).PNG)

![Dataset60-70_Reducer2](https://github.com/illinoistech-itm/ssaxena12/blob/master/ITMD-521/Week-12/Images/Part%203%20a%20(2).PNG)

![Dataset60-70_Reducer4](https://github.com/illinoistech-itm/ssaxena12/blob/master/ITMD-521/Week-12/Images/Part%203%20a%20(3).PNG)

![Dataset60-70_Reducer8](https://github.com/illinoistech-itm/ssaxena12/blob/master/ITMD-521/Week-12/Images/Part%203%20a%20(4).PNG)

##### With Combiner
![Dataset60-70_ReducerCombiner1](https://github.com/illinoistech-itm/ssaxena12/blob/master/ITMD-521/Week-12/Images/Part%203%20b%20(1).PNG)

![Dataset60-70_ReducerCombiner2](https://github.com/illinoistech-itm/ssaxena12/blob/master/ITMD-521/Week-12/Images/Part%203%20b%20(2).PNG)

![Dataset60-70_ReducerCombiner4](https://github.com/illinoistech-itm/ssaxena12/blob/master/ITMD-521/Week-12/Images/Part%203%20b%20(3).PNG)

![Dataset60-70_ReducerCombiner8](https://github.com/illinoistech-itm/ssaxena12/blob/master/ITMD-521/Week-12/Images/Part%203%20b%20(4).PNG)
#### Graph
![Graph Interpretation60-70dataset](https://github.com/illinoistech-itm/ssaxena12/blob/master/ITMD-521/Week-12/Images/Graph%20Part%20-%203(a).PNG)
#### Jobs according to DataSet 60-90.txt

##### Without Combiner
![Dataset60-90_Reducer1](https://github.com/illinoistech-itm/ssaxena12/blob/master/ITMD-521/Week-12/Images/Part%203%20c%20(1).PNG)

![Dataset60-90_Reducer2](https://github.com/illinoistech-itm/ssaxena12/blob/master/ITMD-521/Week-12/Images/Part%203%20c%20(2).PNG)

![Dataset60-90_Reducer4](https://github.com/illinoistech-itm/ssaxena12/blob/master/ITMD-521/Week-12/Images/Part%203%20c%20(3).PNG)

![Dataset60-90_Reducer8](https://github.com/illinoistech-itm/ssaxena12/blob/master/ITMD-521/Week-12/Images/Part%203%20c%20(4).PNG)

##### With Combiner
![Dataset60-90_ReducerCombiner1](https://github.com/illinoistech-itm/ssaxena12/blob/master/ITMD-521/Week-12/Images/Part%203%20d%20(1).PNG)

![Dataset60-90_ReducerCombiner2](https://github.com/illinoistech-itm/ssaxena12/blob/master/ITMD-521/Week-12/Images/Part%203%20d%20(2).PNG)

![Dataset60-90_ReducerCombiner4](https://github.com/illinoistech-itm/ssaxena12/blob/master/ITMD-521/Week-12/Images/Part%203%20d%20(3).PNG)

![Dataset60-90_ReducerCombiner8](https://github.com/illinoistech-itm/ssaxena12/blob/master/ITMD-521/Week-12/Images/Part%203%20d%20(4).PNG)
#### Graph
![Graph Interpretation60-90dataset](https://github.com/illinoistech-itm/ssaxena12/blob/master/ITMD-521/Week-12/Images/Graph%20Part%20-%203(b).PNG)
#### Description
After exectuing 60-70.txt file, the results shows that the execution of jobs takes more time without combiner than jobs which runs with combiner. Also it is to be observed that as the number of reducers increases, the job execution takes a little longer time as the data transfer to multiple reducers take more than than allocation the data to few reducers. 

After execution of 60-90.txt file, it can be observed the jobs takes more execution time without combiner than with a combiner with an exception of first two jobs. It may have happened because the CPU prioritizes the resources on first come first server basis. As multiple jobs may have submitted to the CPU which increses the total execution time. As explained above, more reducers tends to take relatively more time as data transfer takes time. 

Finally it can be inferred that as the number of reducers increases the execution time also increases which is compensated by using combiners which helps in logically allocating data between mappers and reducers. Also, while dealing with large chunks of data, the concept of pre-emptive scheduling comes into play. If there are many jobs running at same time, each will be allocated the CPU resources according to the priority set which leads to high execution time.

#### Reference
https://hadoop.apache.org/docs/r2.6.5/hadoop-yarn/hadoop-yarn-site/FairScheduler.html

## Assumptions

When executing jobs with 1 or multiple reducer, the entire code remains the same exept the job name and allocation of the number of reducer according to the required question.

Formation of JAR and Compilation is carried out by following commands: 
hadoop com.sun.tools.javac.Main MaxTemperature*.java ; 

jar cf mt.jar MaxTemperature*.class ; 

For Part 1, A new Mapper java file named MaxTemperatureMapper4 was created which was executed through the same MaxTemperature.java file using the command:
hadoop jar mt.jar MaxTemperature /user/controller/ncdc/1993/1993.txt /output/shivank_week12_prt1/ncdc/1

For Part 2, 2 Java file were made named MaxTemperature2 and MaxTemperature3WithCombiner. 1 with combiner and the other one without combiner. Both were executed on 1993.txt dataset by altering the number of reducers.
Command without combiner
hadoop jar mt.jar MaxTemperature2 /user/controller/ncdc/1993/1993.txt /output/shivank_week12_prt2/ncdc/3

Command with combiner
hadoop jar mt.jar MaxTemperature2WithCombiner /user/controller/ncdc/1993/1993.txt /output/shivank_week12_prt2/ncdc/5

For part 3, 2 java files were made named MaxTemperature3 and MaxTemperature3WithCombiner which ran on 2 different datasets 60-70.txt and 60-90.txt. The number of reducers were altered in the java file and so does the command according to the dataset.

Command without combiner for dataset 60-70.txt
hadoop jar mt.jar MaxTemperature3 /user/controller/ncdc/60-70/60-70.txt /output/shivank_week12_prt3/ncdc/1

Command with combiner for dataset 60-70.txt
hadoop jar mt.jar MaxTemperature3WithCombiner /user/controller/ncdc/60-70/60-70.txt /output/shivank_week12_prt3/ncdc/5

Command without combiner for dataset 60-90.txt
hadoop jar mt.jar MaxTemperature3 /user/controller/ncdc/60-90/60-90.txt /output/shivank_week12_prt3/ncdc/10

Command with combiner for datset 60-90.txt
hadoop jar mt.jar MaxTemperature3WithCombiner /user/controller/ncdc/60-90/60-90.txt /output/shivank_week12_prt3/ncdc/15
