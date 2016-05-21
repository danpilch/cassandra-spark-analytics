# cassandra-spark-analytics
Supercharge your analysis of Cassandra data with Apache Spark

### Introduction:

[Apache Cassandra](http://cassandra.apache.org/) is a fantastic scalable, fault-tolerant NoSQL database, however it is abhorrently hard to query your data outside the realms of what your datamodel will allow. [Apache Spark](http://spark.apache.org/) is a fast and general engine for large-scale data processing. 

In this guide I intend to demonstrate the power of Spark to provide analysis of your Cassandra data in ways that were possibly thought impossible. This guide is aimed at anyone who is interested in data analysis.

### Requirements:

This guide has been tested with the software versions outlined below. Older versions may work, test at your own risk. 

This guide was developed using [CentOS 7](https://www.centos.org/).

| Software | Version |
| --- | --- |
| [Cassandra](http://cassandra.apache.org/) | `2.2.5` |
| [Cassandra Spark Connector](https://github.com/datastax/spark-cassandra-connector) | `1.5` |
| [Spark](http://spark.apache.org/) | `1.6.1` |
| [Docker](https://www.docker.com/) | `1.11.11` |
| [Docker-compose](https://docs.docker.com/compose/) | `1.7.1` |
| [Python](https://www.python.org/) | `2.7.5` |

### Setup
