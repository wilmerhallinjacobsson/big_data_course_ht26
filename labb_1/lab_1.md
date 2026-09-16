# Big Data: Lab 1

### First error
**The cause:** bitnami’s spark image is no longer being updated and have therefore been moved to bitnamilegacy/spark on docker hub.

![Image of first error in terminal.](./images/first_error_image.png)

**The solution:** Change the name from bitnami/spark to bitnamilegacy/spark in the command: ```docker pull bitnamilegacy/spark.```

Also adding "legacy" in the following commands.
```
docker run -d --name spark-master -h spark-master -p 8080:8080 bitnamilegacy/spark
```

```
docker run -d --name spark-worker -h spark-worker --link spark-master:spark-master bitnamilegacy/spark /opt/bitnami/spark/bin/spark-class org.apache.spark.deploy.worker.Worker spark://spark-master:7077
```

### Second error
While attempting to run the spark-submit command: ```/opt/bitnami/spark/bin/spark-submit --master spark://spark-master:7077 /opt/bitnami/spark/simple_dataframe.py``` 
I got the following error: 
![Image of first error in terminal.](./images/second_error_image.png)





