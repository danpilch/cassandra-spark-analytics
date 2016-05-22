FROM anapsix/alpine-java:jdk8
MAINTAINER Dan Pilch (danielpilch@hotmail.co.uk)

ENV SPARK_VERSION=spark-1.6.1-bin-hadoop2.6 \
        SPARK_CASSANDRA_CONNECTOR_VERSION=1.5.0

# Create temporary spark runtime dir 
RUN mkdir -p /tmp/spark-events

# Install deps
RUN apk update && apk add bash curl tar git openssh htop vim python python-dev

# Generate keys
RUN mkdir -p /root/.ssh && \
        chmod 700 /root/.ssh/ && \
        echo -e "Port 22\n" >> /etc/ssh/sshd_config && \
        cp -a /etc/ssh /etc/ssh.cache && \
        /usr/bin/ssh-keygen -A && \
        echo -e "\n\n\n" | ssh-keygen -t rsa && \
        cat /root/.ssh/id_rsa.pub > /root/.ssh/authorized_keys && \
        ssh-keyscan -H localhost,127.0.0.1 >> /root/.ssh/known_hosts && \
        ssh-keyscan -H 127.0.0.1 >> /root/.ssh/known_hosts && \
        ssh-keyscan -H localhost >> /root/.ssh/known_hosts

# Download, extract and symlink spark
RUN curl http://d3kbcqa49mib13.cloudfront.net/${SPARK_VERSION}.tgz | tar xz && \
        ln -sf /${SPARK_VERSION}/ spark

# Git clone and compile Spark Cassandra Connector and add it to spark
RUN git clone https://github.com/datastax/spark-cassandra-connector.git && \
        cd spark-cassandra-connector && \
        git checkout v${SPARK_CASSANDRA_CONNECTOR_VERSION} && \
        sbt/sbt assembly && \
        mv /spark-cassandra-connector/spark-cassandra-connector/target/scala-2.10/spark-cassandra-connector-assembly-${SPARK_CASSANDRA_CONNECTOR_VERSION}.jar /spark/ && \
        rm -rf /spark-cassandra-connector && \
        /spark/bin/spark-shell --jars /spark/spark-cassandra-connector-assembly-${SPARK_CASSANDRA_CONNECTOR_VERSION}.jar && \
        echo "JAVA_HOME=/opt/jdk" >> /spark/conf/spark-env.sh && chmod +x /spark/conf/spark-env.sh

# Create spark-defaults.conf
RUN echo -e "spark.eventLog.enabled true\nspark.driver.extraClassPath /spark/spark-cassandra-connector-assembly-1.5.0.jar\nspark.executor.extraClassPath /spark/spark-cassandra-connector-assembly-1.5.0.jar" >> spark/conf/spark-defaults.conf

# Create start.sh
RUN echo -e "#\!/bin/bash\n\n/usr/sbin/sshd -D -f /etc/ssh/sshd_config &\n\n/spark/sbin/start-all.sh\n\n/spark/sbin/start-slave.sh spark://`hostname -i`:7077\n\ntail -f /spark/logs/*" >> start.sh && \
        chmod +x start.sh

# Start Spark
CMD ["/bin/bash", "start.sh"]


