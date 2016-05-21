# cassandra-spark-analytics
Supercharge your analysis of Cassandra data with Apache Spark

## Introduction

[Apache Cassandra](http://cassandra.apache.org/) is a fantastic scalable, fault-tolerant NoSQL database, however it is abhorrently hard to query your data outside the realms of what your datamodel will allow. [Apache Spark](http://spark.apache.org/) is a fast and general engine for large-scale data processing. 

In this guide I intend to demonstrate the power of Spark to provide analysis of your Cassandra data in ways that were possibly thought impossible. This guide is aimed at anyone who is interested in data analysis.

## Requirements

This guide has been tested with the software versions outlined below. Older versions may work, test at your own risk. 

This guide was developed using [CentOS 7](https://www.centos.org/).

| Software | Version |
| --- | --- |
| [Cassandra](http://cassandra.apache.org/) | `2.2.5` |
| [Cassandra Spark Connector](https://github.com/datastax/spark-cassandra-connector) | `1.5` |
| [Spark](http://spark.apache.org/) | `1.6.1` |
| [Docker](https://www.docker.com/) | `1.11.1` |
| [Docker-compose](https://docs.docker.com/compose/) | `1.7.1` |
| [Python](https://www.python.org/) | `2.7.5` |

## Setup

### Docker:
Firstly we need `docker` and `docker-compose`  installed and running. A good startup guide can be viewed [here](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-centos-7).

Check docker is functioning correctly by issuing command `docker ps`.

### Cassandra:

#### Start Cassandra container

We will start Cassandra with the included `compose/cassandra.yml` instruction file. This file can be edited if you know what you are doing but the defaults are fairly sane for this demo. The Cassandra Thrift port (9160) will bind to `127.0.0.1:9160` we will use this to connect to cassandra via `cqlsh` from the host.

`docker-compose -f compose/cassandra.yml up -d`

Check the container has started with `docker ps`.

#### Install Cqlsh

Install `cqlsh` with command `pip install --user cqlsh`.

Test you can access cassandra correctly:

`cqlsh 127.0.0.1:9042`

### Spark

we will start Spark with the included `compose/spark.yml` instruction file. This file can be edited if you know what you are doing but the defaults are fairly sane for this demo.

`docker-compose -f compose/spark.yml up -d`

Check the container has started with `docker ps`.
