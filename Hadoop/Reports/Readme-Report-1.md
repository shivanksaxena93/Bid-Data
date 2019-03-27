# Meetup Report #1

## Introduction to Distributed Big Data Processing with Hadoop
#### -Organized by Coding Temple (April 4, 2018)

### Summary

The talk started with a detailed introduction of HDFS also known to be as Hadoop distributed file system. Hadoop was originally designed to process complex data operations such as filetring ,merging, transformation and aggregation on multi computer platform. Distributed word expands the concept of data storage technologies which allows storage of data away from the client site. File system defines the way of organizing files on any system.

A deeper insight of hadoop cluster explained us about the independency of data organizing in rows and columns. In HDFS, machines does not share memory of induvidual systems and it also cannot be accessed randomly giving out segmentation error. Data is splitted on cluster by hadoop only in rows and in case of failure of any single machine, hadoop retrives the data by fetching the copy of data segments.

The lecture then described the prioritizing of jobs on a cluster. It is done by generating of queues which are passed on hadoop through resource manager which gets the resources and jobs based on their priorities.Different types of nodes were defined including Head nodes, Edge Nodes and worker nodes as hadoop uses the concelpt of master slave relation. A Head node is the most responsible authority for making decision parallely monotring logics and data processing. In Edge nodes no processing of data takes places and is only used for issuing for commands for worker nodes. Edge nodes also helps you to be on hadoop cluster without making you being on worker nodes which processe the data.

Also the concept of Dataskew was explained which describes the crasing of nodes because of receiving of data more than the capacity allocated by the head node. Later, a brief description about SPARK was given. SPARK is a distributed Analytics Engine which splits the execution into stages which are seperated by the shuffles. A major difference between Hadoop and SPARk was discussed which was Haddop is written in JAVA whereas SPARK is written in SCALA.

### Conclusion

It can be concluded that HDFS is a distributed file storage system where as Spark deals with data which is already distributed by using Map and Reduce. Also we got to know that because hadoop is written in java therefore it requirres serialization.


In short managing Big Data is the new REALITY..!!

 ### Observations 
 
 Different industry leader came under a single roof to share their wealth of knowledge and make good connections. Different problems raised by different individuals gave us an insight view of error handling while working on big data.
 
 ### Comments about the subject
 
 It was very interesting topic of the meet up which gave us the opportunity to learn Hadoop and techinques to handle big data. The topics were started from the very basic and were explained in depth which helped us clear our concecpts.
 
