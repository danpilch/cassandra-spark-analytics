from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext, Row


if __name__ == '__main__':
    # Define Spark configuration
    conf = SparkConf()
    conf.setAppName("spark_demo")
    conf.set("spark.cassandra.connection.host", "CASSANDRA_DOCKER_IP")
    conf.set("spark.cassandra.auth.username", "username")
    conf.set("spark.cassandra.auth.password", "password")

    # Define the Cassandra keyspace and column family to query
    keyspace = "spark_demo"
    table = "person_data"

    spark_context = SparkContext(conf=conf)
    sql_context = SQLContext(spark_context)

    data_frame = sql_context.read.format("org.apache.spark.sql.cassandra") \
            .options(keyspace=keyspace, table=table).load()

    sql_context.registerDataFrameAsTable(data_frame, table)

    # Perform an SQL query against the Spark data frame
    query = sql_context.sql("""SELECT first_name, count(*) as count from person_data group by first_name order by count desc""")
    
    # Show the output via sql_context (top 25)
    query.show(25)

    spark_context.stop()
