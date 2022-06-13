# PySpark Primer.
Source: LinkedIn Learning : Apache PySpark by example - Jonathan Fernandes.
***
# 1) Introduction to Apache Spark.

## 1.1 The Apache Spark ecosystem.

Spark runs locally as well as in a cluster, on-premise, or in a cloud.

### Apache Spark Ecosystem.
* Spark Core API is the foundation of the Apache Spark Ecosystem.
	* It consists of Spark SQL and data frames,
	* Streaming for real-time data,
	* MLlib for machine learning, and
	* GraphX for graph structure data at scale.
![79d193bf9a98c609a3cc2b5e4c6949b1.png](/images/79d193bf9a98c609a3cc2b5e4c6949b1.png)

### Spark Core API
* Task Scheduling
* memory management.
* fault recovery
* interacting with storage systems
* Spark is primarily written in Scala, but we can use Java, Python, R and Sql.

### Spark SQL and Dataframes
* Dataframe programming abstraction,.
* Complex analytics with SQL.

### Spark streaming.
* process real-time data.
* Spark streaming is running on top of Spark, it provides powerful interactive and analytical applications across both *streaming and historical data*.
* use similar code for batch data and real-time data.

### MLlib
* provides scalable machine learning
* works in memory, hence is way faster than Hadoop's MapReduce.

### Graph X
* enables working with graph-structured data at scale.
* introduces a new graph abstraction, the directed multigraph
* useful for visualizing graphs like in social network.

Spark is a comprehensive and self sufficient ecosystem.
***
## 1.2 Why Spark?

### What is PySpark?
is just a python wrapper around the spark core.

Why spark is considered over the following:
* **Pandas**
	* tabular data
	* can handle hundreds of thousands to millions of rows
	* mature and feature rich
	* however, *limited* to a single machine(has no distributed computing capabilities)
* **Hadoop**
	* it was the big data platform,
	* it has a compute system(mapreduce) and storage system(HDFS) closely integrated.
	* HDFS for fault tolerance with replication capabilities.
	* Spark however can do it in memory, whereas Hadoop has to read from and write to disk.
		* Hence Spark is preferred platform nowadays.
		* Spark requires more RAM and hence setting up Spark clusters can be more expensive.
* **Dask**
	* library for parallel computing in Python.
	* ![c0be0af7403af05429b689566a60b1d5.png](/images/c0be0af7403af05429b689566a60b1d5.png)
	* ![58ec2dd250dd931ee9a2974130fa1c3b.png](/images/58ec2dd250dd931ee9a2974130fa1c3b.png)

***
## 1.3 Spark origins and Databricks.

Spark creators knew that MapReduce was *inefficient* for iterative and interactive computing jobs.
So right from beginning, Spark was created to be fast for interactive queries and iterative algorithms. They incorporated ideas like
* in-memory storage
* and efficient fault recovery.

**Databricks** offers Apache spark with a platform that unifies the data science and data engineering. 
It provides an optimized version of Apache Spark, it offers interactive notebooks, and it provides full enterprise security for large scale organizations.

They also offers various connectors to Business Intelligence tools.
***
## 1.4 Spark Components.

* The **Driver** sits on the node on the cluster.
	* it maintains info about the Spark application.
	* like it'll respond to a users program or input.
	* it distributes and schedules work across the Executors.
	* maintains all essential/relevant information.
* The **Executors**  on the Worker Nodes carries out the work
	* that's been assigned by the Driver and reports back on the state of the computation, back to the Driver.
* The Driver and the Executors are just processes
	* which means they can exist on one machine(local nodes) or run on different machines if they're in a cluster.
* Finally, the **Cluster Manager** 
	* is a task manager or a resource manager.
	* when you submit Spark applications to cluster Managers, they'll grant resources to your applications so that the work can be completed.

![f4a2327f1423c7ce020f2ae0a1c9f38d.png](/images/f4a2327f1423c7ce020f2ae0a1c9f38d.png)

### Cluster Manager types:
* Standalone option,
* Apache Mesos - general cluster manager
* Hadoop YARN - general cluster manager
* Kubernetes - to automate to the deployment and management of containerized applications.

### Creating a SparkSession:
* creating a Spark session is the first step of any Spark application
* With Spark 2.0, a spark session can access all of	Spark's	functionality(Spark and SQL context) through a single, unified point of entry.

***
## 1.5 Partitions, transformations, lazy evaluations and actions.

### Partitions:
if we want the spark workers to work in parallel, Spark needs to break the data into chunks or partitions.
* a **partition** is a collection of rows from your data frame that sits on one machine in your cluster.
* a data frames partition is how data is physically distributed across the cluster of machines during execution.
* however we users don't normally get into the manipulating of partitions manually. That part is abastracted from us.
* having only a single partition, Spark can't parallelize jobs even if you have a cluster of machines available.
* if you have several partitions, but only one worker, spark can't parallelize jobs as there is only one resource that can do the computation.

### Transformations:
* core data structure in Spark.
* are **immutable**
* instructions that we use to modify the data frame are known as transformations. 
	* could be a filter operation, or a distinct operation
	* when we perform a transformation operation, nothing seems to happen as
	* Spark **doesn't act on transformations** until we perform something called *actions*.

### lazy evaluation.
when an operation is performed on your data, Spark doesn't work on modifying the data straight away. 
Instead it builds a plan of transformations that will be performed on the data.
**This waiting until the last moment to do work is known as lazy evaluation.**

It's helpful because it allows spark to create a streamlined plan, allowing it to run as efficiently as possible across the cluster. 

Lazy evaluations is pretty efficient and as transformations are immutable, so instead of making unecessary changes, it finds the least effort to perform that operation.

### Actions:
tells spark to compute the results of these transformations, and there are three types:
* View Data: .show()
* Collect Data: .collect()
* Write data: .write.format(...)

***
# 2) Working with the DataFrame API.

## 2.1 The DataFrame API.

![feb0b735c78f865c17d67919f0858419.png](/images/feb0b735c78f865c17d67919f0858419.png)

* In Spark, a DataFrame is a distributed collection of objects of type row. Like a table.
* however, a Spark DataFrame could sit across hundreds of computers.

### The Dataset API:
* Datasets are used with statically typed languages.(java or scala)
* python(dynamically typed language) doesn't support the Dataset API

***
## 2.2 Working with DataFrames.

![c9045e177daa8544a83eedf63cc7bd54.png](/images/c9045e177daa8544a83eedf63cc7bd54.png)

![bbde7da824e23553137b3d0ab363ee84.png](/images/bbde7da824e23553137b3d0ab363ee84.png)

![a966c702eb2c24177775bc8314e788a2.png](/images/a966c702eb2c24177775bc8314e788a2.png)

***
## 2.3 Schemas.

A schema defines the column names and what data types they are.
![c90f4c20028db089d8ecb2da4f4b9d19.png](/images/c90f4c20028db089d8ecb2da4f4b9d19.png)

### Schema:
* spark can infer the schema by default, although,
	* explicitly defining the schema in Spark is recommended.
* import the different data types from pyspark.sql.types
* ![0d6cce3f3a2b86ceb038fbfd6a136098.png](/images/0d6cce3f3a2b86ceb038fbfd6a136098.png)

***
## 2.4 Working with columns.

![9b4e80861fbd7a229d04e71e1552acd8.png](/images/9b4e80861fbd7a229d04e71e1552acd8.png)

![df3eced38116afe4f7c8b58be73556e0.png](/images/df3eced38116afe4f7c8b58be73556e0.png)

![76c7c786762b63ea22fab121d7fab56f.png](/images/76c7c786762b63ea22fab121d7fab56f.png)

![96b0af6eae871e10754b3a4b5e31ed98.png](/images/96b0af6eae871e10754b3a4b5e31ed98.png)

![7d84553f865a4e49852d5c16796dc34b.png](/images/7d84553f865a4e49852d5c16796dc34b.png)

![2f63053496b1a59df4219a2bfaceaed9.png](/images/2f63053496b1a59df4219a2bfaceaed9.png)

![f70925b92453422969097b56c2632ba5.png](/images/f70925b92453422969097b56c2632ba5.png)

***
## 2.5 Working with rows.

![b138d9f2a8a5dbf46ac9186a8aaf6187.png](/images/b138d9f2a8a5dbf46ac9186a8aaf6187.png)

![c558eea7add0211394914a2132055eff.png](/images/c558eea7add0211394914a2132055eff.png)

![7f8af3b255169fc29ca53ac8ac9d0e96.png](/images/7f8af3b255169fc29ca53ac8ac9d0e96.png)

![d7838f4ceeb678fae9a25815783ff48d.png](/images/d7838f4ceeb678fae9a25815783ff48d.png)

***
# 3) Functions.

## 3.1 Built-in functions.

![e8239b097278455dadcb69bf85249974.png](/images/e8239b097278455dadcb69bf85249974.png)

![82eabfef3cae9df715c6d1b3fbd7ee17.png](/images/82eabfef3cae9df715c6d1b3fbd7ee17.png)

***
## 3.2 User-defined functions.

![b478746fd8765af50a9156992540c4cd.png](/images/b478746fd8765af50a9156992540c4cd.png)

when creating user defined functions in python , there is a penalty in computation. so it is preferred to create functions in scala or java.

***
## 3.3 Working with Joins.

![9aa931c759aa7e39fbd2d55cc7901405.png](/images/9aa931c759aa7e39fbd2d55cc7901405.png)

![1838cab9de49e7d1c184942eba57fa49.png](/images/1838cab9de49e7d1c184942eba57fa49.png)

***
# 4) Resilient Distributed Datasets(RDDs).

## 4.1 RDDs.

An RDD is an *immutable* partitioned collection of records that can be worked on in parallel.

In RDD, the records are just python, scala or java objects.
![4adb31d12652c837fd2829dc7bce60a4.png](/images/4adb31d12652c837fd2829dc7bce60a4.png)

However, the challenges with the object types is:
![24d983b9ca8f39373747d44676ee4d37.png](/images/24d983b9ca8f39373747d44676ee4d37.png)

![4b9e8f324e32a7964cc2feecb2364b66.png](/images/4b9e8f324e32a7964cc2feecb2364b66.png)

![5f992c720eab677325532fd8f7f5716c.png](/images/5f992c720eab677325532fd8f7f5716c.png)

RDDs are powerful but lack optimizations. Don't have the built in functions too.

![f506678181589f9fddbd61cfb039a3c8.png](/images/f506678181589f9fddbd61cfb039a3c8.png)

***
Source: <https://www.youtube.com/watch?v=YvTzvZh3yTE&list=PL7_h0bRfL52qWoCcS18nXcT1s-5rSa1yp&index=2>

Master Databricks and Apache Spark by Bryan Cafferky.
***
# Lesson 1.

![252f3fe284e5d4d5bd5f100bbe0a020c.png](/images/252f3fe284e5d4d5bd5f100bbe0a020c.png)

Spark isn't a storage engine. It is a platform that enables parallel processing/distributed processing.

![dae516b5030538cdb4ad3cb0ae9be659.png](/images/dae516b5030538cdb4ad3cb0ae9be659.png)

# Lesson 2.

## HDInsights.

![3df017f874699aa0efc7b7f421e6669d.png](/images/3df017f874699aa0efc7b7f421e6669d.png)

# Lesson 3.

## The Data Science Process.

![c31d905949a0f307a30fcb9bc02b2f48.png](/images/c31d905949a0f307a30fcb9bc02b2f48.png)

# Lesson 4.

## Spark SQL:
![4e65171c6b9989f05a04889df2a9f48a.png](/images/4e65171c6b9989f05a04889df2a9f48a.png)

![d66edb7a63024fecea26582ea3cee2e8.png](/images/d66edb7a63024fecea26582ea3cee2e8.png)

![feeb8539c5778abae78b90c8943e6e55.png](/images/feeb8539c5778abae78b90c8943e6e55.png)

## Delta Lake
![1e138ffbae6a0120ada7f01079073290.png](/images/1e138ffbae6a0120ada7f01079073290.png)

# Lesson 5.

## Spark SQL Data Definition Language.

