Source: <https://www.youtube.com/watch?v=qWru-b6m030>
***
# Data Engineering Primer

# How data engineering works?

## The Excel method:

* Multiple data sources >> manually collect and organize data in the required format >> developer uses excel to extract meaningful insights and do visualizations manually >> end user gets to see his/her report.

![f694985b6de417eca0d7e8a20afb8f54.png](/images/f694985b6de417eca0d7e8a20afb8f54.png)
***
## ETL pipeline.

To automate the above process, Data engineer builds a pipeline.
### Extract:
* set up an API connection to all the data sources.

### Transform:
* remove errors from the data,
* change it to required format.
* map the same types of records to each other
* data validation.

### Load:
* Load the processed data to a database(MySQL, etc)

### BI tools:
* Power BI, Tableau can be used to present the visualization to end Analytic user.


The data engineer will build a script to run this entire operation in a batch wise so the above task can be automated and the end user gets the report without any intervention of human being.
![f0a12c6547042894909e674e44e83a18.png](/images/f0a12c6547042894909e674e44e83a18.png)

### Problems with the above ETL pipeline setup:
* The above pipeline fails when the data size starts to increase.
* Standard **transactional DBs** (mysql), are optimized to perform write operations, they are very resilient and are great to run apps,
	* however they aren't optimized to do analytical jobs
	* they suffer when processing complex queries.

***
## Data Warehouse.

Instead of a standard DB, the new place to keep the consolidated data from multiple sources, is *Data Warehouse*.
![da72dcc97f724f6fc0154a027d9db607.png](/images/da72dcc97f724f6fc0154a027d9db607.png)

* Data Warehouse is a *repository* that consolidates data from all sources in a single central place.
* idea of a warehouse is to structure/organize data that gets into tables and then tables into *schemas*(relationships between tables.)
![ca88696e053440109e6d3e610f00dea9.png](/images/ca88696e053440109e6d3e610f00dea9.png)

### Main difference between warehouse and database:

Warehouse is specifically optimized to run complex analytics queries as opposed to simple transaction queries of a regular database.

### The pipeline with Warehous:
* data is generated at sources,
* automatically pulled by ETL scripts, transformed and validated on the way,
* finally populates the tables inside the warehouse.

***
## Data Lakes.

What happens to this pipeline/process when a Data Scientist is involved. How do Data Scientist's and Data Engineers collaborate.

### Data Scientist:
* job is to find hidden insights in data and make predictive models to forecast the future.
* a *data warehouse* may not be enough for these tasks.
	* because it is structured around reporting on the metrics that are *defined in advance*.

To fix this issue, Data Engineers could build **custom ETL pipelines** to assist the Data Scientists.
![ca600a3ba4c01c623a22b19de4116f46.png](/images/ca600a3ba4c01c623a22b19de4116f46.png)

or, we can use the ...
### Data Lake:
* data lake is the complete opposite of data warehouse.
* keeps all the data raw without preprocessing it and imposing a defined schema.
* Follows the **ELT(Extract, Load, Transform)** model.
	* because it's the data scientist who gets to decide how to transform the data as per their model requirements.
![8782e36d0098db13772a59edf7119fbd.png](/images/8782e36d0098db13772a59edf7119fbd.png)

Hence, the job of Data Engineer is to enable the constant supply of info into the data lake.
***
## What is Big Data.

### 4V's of big data:
* Volume(big),
* Variety(both structured and unstructured),
* Veracity(requires quality control),
* Velocity(real-time)

Cue to...
***
## Data Streaming.

Upto this moment, we've only discussed *batch data*, which means that there is some schedule involved from data extraction to transformation.

However, there are applications and usecases where the new data is generated by the second and we need to stream it to the analytical systems right away.

### Publish/Subscribe communication:
* **Synchronous communication**, where data provider and system(that wants the data) communicate over API.
	* this type is based on the *request-respone* model. \
	* This gets incredibly slow when huge volume of data is involved.
![c8635443675a1f50f3e032bd703122f1.png](/images/c8635443675a1f50f3e032bd703122f1.png)

* **Assynchronous communication**, the pub/sub model enables assynchronous conversation between multiple systems that generates a lot of data simultaneously
	* it decouples data sources from data consumers
	* the data is divided into different topics/profiles.
	* data consumers that subcribes to these topics, when a new data record or an event is generated, it's published inside the topic,
	* allowing the subscribers to consume this data at their own pace.
	* This way there is no waiting between systems to send messages.
![87cf656e8a379a7bacc995ec6f631106.png](/images/87cf656e8a379a7bacc995ec6f631106.png)
* **Kafka** is the most popular pub/sub tech.
***
## Distributed computing.
* petabytes of data are stored in several servers(sometimes thousands) called as *Server Cluster*.
* **Hadoop** is a technology used for distributed storage.
	* framework that allows the storing of data in clusters.
	* higly scalable
	* offers much redundancy for securing info
* **Spark** is a popular *data processing* framework.
	* it helps operate hadoop clusters.

Finally the big data engineering pipeline looks like:
![9d883f11f2fe6277b1d498ae5aa4ebce.png](/images/9d883f11f2fe6277b1d498ae5aa4ebce.png)
***
