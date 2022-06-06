# Apache Kafka Primer
Source: LinkedIn Learning - Apache Kafka Essential Training by Kumaran Ponnambalam.
***
# 1) Introduction to Kafka.

## 1.1 Message queues.

### Publish Subscribe with Message Queues.

![8331b6c19254043d236ed496cd0bd1c5.png](/apache_kafka/images/8331b6c19254043d236ed496cd0bd1c5.png)

This is a *clean and scalable solution* 
* Each sender only needs to know about the message queue and simply publish the messages to the queue.
* a receiver becomes a subcriber and subscribes to the message queue.
	* When a new message appears in the queue, the subscriber is notified, who then proceeds to pull the message and use it.
* In this case, each of the publishers and subscribers only need to know about the message queue.
	* they are unaware of the other pubs and subs using the same queue.

### pub-sub advantages:
* decoupling of publishers and subscribers.
	* easy management and changes.
* Scaling (N+1)
* MQs also provide *Back-pressure handling*.
	* if the publishers generate data in spikes, the MQs can act as a buffer zone to cache data until the subs catch up and process them.
* MQs also provide *reliability*  thru persistent queue data and tracking consumption of data.

***
## 1.2 What is Kafka?

* Kafka is an events/messages Streaming Platform.
	* events/messages represents the actual data that is exchanged through kafka.
* critical piece of the big data puzzle.
* it is open-source with commercial options.
* arguably the most popular messaging platform in the world.
* **Producers** (pubs) push messages to kafka.
* **Consumers**(subs) listen and receive messages.

### Kafka Data Functions:

![80a9ade641b7fd8cd2d6905b20b9060f.png](/apache_kafka/images/80a9ade641b7fd8cd2d6905b20b9060f.png)

* it *collects* messages from multiple producers concurrently.
* it provides *persistent* storage of the messages received, which provides fault tolerance capabilities.
* it *transports* data across from producers to consumers.
	* with mirroring capabilities, it can also transport across networks.
* it *distribues* data across multiple concurrent consumers.
* it provides *tracking of message* consumption by each consumer.
***

## 1.3 Benefits of Kafka.

* provides *high throughput* and can handle large quantities of data.
* low *latencty* of a few milliseconds
* provides excellent *fault tolerance* against failures, either within Kafka or with consumers.
* *decouples* producers and consumers; they do not need to know about each other; makes management easier and enables better software development.
* *Back-pressure handling*.
* provides *Horizontal scalability*.
* Streaming and Batching possible in kakfka; 
	* low latency: enables stream processing.
	* store and forward capability: enables batch processing.
***
## 1.4 Kafka use cases.

![540ba54d0fe68b30fdbf0ef12310c189.png](/apache_kafka/images/540ba54d0fe68b30fdbf0ef12310c189.png)

***
## 1.5 Chapter Quiz.

### Which of the following is NOT a kafka data function?
A) processing is the answer.
Other options given were: storage, tracking data consumption, collection.

### What does back pressure handling in Kafka mean?
A) Kafka can cache data until the consumer is ready to receive & process it.

### Which of the following is an important use case for Kafka?
A) event sourcing is the answer.
Other options: state management, graph database, video player.
***
# 2) Basic concepts.

## 2.1 Messages.

### Kafka messages:
is the unit of data that is collected, stored and distributed by Kafka.
* it's also called an *event*.
	* a message is a record of a real world event at a point in time.
* it can also be any unit of data:
	* equivalent to a row or record in a DB.
	* it can hava attributes and values like a map;
	* a blob or an audio snippet.
* Kafka treats all messages as a **byte array**.
	* structure imposed by Pub, understood by Consumer.
* Size limit exists in Kafka.

### Messages content:
Kafka does have some pre-defined attributes.
* messages in kafka have a **key**, which is defined by the producer of the message.
	* key's are not *mandatory* and they also *need not be unique*.
	* used for partitioning of data.
* Value attribute contains the *actual message*.
	* user defined.
* Another important attribute is: *timestamp*
	* it is automatically timestamped.
	* **event time**: when message producer creates a timestamp.
	* **ingestion time**: is where kafka broker timestamps it, when it stores the record.
***
## 2.2 Topics.

### What is topics in kafka?

![1423982a32bbde82d72a2999eb6cbc3e.png](/apache_kafka/images/1423982a32bbde82d72a2999eb6cbc3e.png)

partitions in topics - eg.
![1ea67d6750e8cc02eb21660f344bcd02.png](/apache_kafka/images/1ea67d6750e8cc02eb21660f344bcd02.png)

***
## 2.3 Kafka brokers.

A kafka broker is the central brain behind everything that kafka does.

* it is a running instance of kafka.
	* it is a physical process that runs on the base of OS and executes all kafka functions.
* listens on a specific port.
	* usually it is port 9092 but it's configurable.
* receives messages from producers and stores them locally in logs.
* performs subscription management.
	* keeps track of all active consumers
	* it knows about the last message that was sent to a consumer,
	* so only sends any new messages in the subscribe topic.
* performs topics, partitions & logs management.
* multiple kafka brokers can be clustered together to form a single Kafka cluster.
* a kafka broker also takes care of *replicating* topic partitions across multiple brokers.
	* provides fault tolerance.

***
## 2.4 Logs in kafka.

* Kafka logs are the *physical* files	in which data is stored before they are consumed by the consumers.
* logs are managed by kafka brokers.
	* each broker has an assigned log directory, where it stores the log files.
* multiple log files(by broker/topic/partition).
* *rolling files* ; so when a file gets filled up, it's rolled over and a new file is created to continue with the logging process.
* Data in kafka is only kept for a *configured* interval of time.
	* default is 7 days.
	* a seperate thread in kafka keeps pruning files that are over this period.
* performs physical space management.
* All configuration for kafka is in the *server.properties* file. 
***
## 2.5 Producers and Consumers.
### Producers:
![1aa3ac9a753c6ae19c153ab8ba4c05af.png](/apache_kafka/images/1aa3ac9a753c6ae19c153ab8ba4c05af.png)

### Consumers:
![839abf21dc0ba0f3033faaffa18855a2.png](/apache_kafka/images/839abf21dc0ba0f3033faaffa18855a2.png)

***
## 2.6 Role of ZooKeeper.

Every kafka instance or cluster needs an instance of Zookeeper deployed along with it.

### Purpose of ZooKeeper?
* Every kafka instance/cluster needs ZooKeeper.
	* zookeeper is a *centralilzed* service that is used for storing configuration info as well as helping with *distributed* sync.
* central, real-time info store for kafka
* helps in broker management
	* broker registry.
	* active controller.
* topic management.
***
# 3) Using the kafka Command line.

## 3.1 Chapter quiz.

### Which of the following is an optional parameter for creating a topic?
A) retention.ms

### If you have multiple producers and consumers, how can you route a message from a specific producer instance to a specific consumer instance?
A) it is not possible.

### How many Leaders can a single partition have?
A) 1

### Which of the configuration parameters in the server.properties file is used to specify the physical log file location?
A) log.dirs

### Partitions in Kafka are numbered ______.
A) 0 to N

### The bootstrap-server parameter is used to provide ______ to the shell command.
A) a list of Kafka brokers.

### In which directory (under the Kafka root installation directory ) would you find the Kafka client scripts ?
A) bin
***

# 4) Kafka Partitions and Groups.

## 4.1 Intro to partitions.

![4fefb05e8676e85918c6581578706439.png](/apache_kafka/images/4fefb05e8676e85918c6581578706439.png)

* partitions can be replicated(for fault tolerance).
* partitions allow Kafka to scale(horizontal scaling).

![a29b293061b94f0e75ae8ded328e2b3e.png](/apache_kafka/images/a29b293061b94f0e75ae8ded328e2b3e.png)

***
## 4.2 Consumer groups.

### What is it?
* a group of consumers who share a topic workload.
	* a topic may be generating thousands of messages in a short amount of time.
	* it may not be possible for one single consumer process to keep up with these messages.
	* for scalability, multiple consumer processes can be started and the messages can be distributed among them for load balancing.
* each message goes to only one consumer in a group.
* consumers split workload through partitions.
	* kafka only considers the number of partitions for distribution, not the number of messages expected in each partition.
	* no. of partitions >= no. of consumers.
* multiple consumer groups - each group gets all messages.
* brokers track and rebalance consumers.

![b167b4352fca084560df5e703400e1de.png](/apache_kafka/images/b167b4352fca084560df5e703400e1de.png)

***
## 4.3 Consumer offset management.

![4617b6b32993de7234d1689d4052ba0e.png](/apache_kafka/images/4617b6b32993de7234d1689d4052ba0e.png)

***
## 4.4 Chapter quiz.

### Which of the following is NOT true about partitions?
A) A partition can belong to multiple topics.

### Kafka guarantees message ordering within a given _____ .
A) Partition.

### What are the limitations for changing the number of partitions after topic creation?
A) It's not possible to change at all.

### Which of the following is NOT a benefit of Offsets in Kafka ?
A) It is used to allocate partitions to consumers in a consumer group.

### In the output of kafka-consumer-groups.sh, the value of "lag" will keep increasing when ______ .
A) consumers are not keeping up with the speed of publishers.

### What happens if the number of consumers in a consumer group is higher than the number of partitions?
A) Some of the consumers will be starved, with no partitions allocated to them.

***

Source: Apache kafka for beginners, <https://www.youtube.com/watch?v=d3ZDUBFB91I&list=PLt1SIbA8guusxiHz9bveV-UHs_biWFegU&index=2>
***
![116badf0d110103512a85699a7768040.png](/apache_kafka/images/116badf0d110103512a85699a7768040.png)

![25198849546f7f47c7c931b427aaae4a.png](/apache_kafka/images/25198849546f7f47c7c931b427aaae4a.png)

![b55ee360d8b09835afe663711829aa6d.png](/apache_kafka/images/b55ee360d8b09835afe663711829aa6d.png)

![7c60b6283fde90950d7164dc67b86e07.png](/apache_kafka/images/7c60b6283fde90950d7164dc67b86e07.png)

![f930ab0e70ae7551b6e5682c1a96bb48.png](/apache_kafka/images/f930ab0e70ae7551b6e5682c1a96bb48.png)

![1b8ae41147e79fac1e350752a520ec8e.png](/apache_kafka/images/1b8ae41147e79fac1e350752a520ec8e.png)

![4cb7bb1d6c67e9803c70319e8e13ba7a.png](/apache_kafka/images/4cb7bb1d6c67e9803c70319e8e13ba7a.png)

![eef5194493b1838575e4bd66964a37b6.png](/apache_kafka/images/eef5194493b1838575e4bd66964a37b6.png)

![a8b7fa24c731c6c421598da63b7f8d13.png](/apache_kafka/images/a8b7fa24c731c6c421598da63b7f8d13.png)

![4ebbb06a2812962560c7e80d80c4a71b.png](/apache_kafka/images/4ebbb06a2812962560c7e80d80c4a71b.png)

![4f791c37fcdf568db46c42ad7d1694a7.png](/apache_kafka/images/4f791c37fcdf568db46c42ad7d1694a7.png)

![8f36be35898ff28b60fe240443f38164.png](/apache_kafka/images/8f36be35898ff28b60fe240443f38164.png)
***