# lab 3

Use docker compose to create an image and a compose of a worker and a master and a network.
```
docker compose up -d --build
```

Start a listener to port 9999.
```
docker compose exec master nc -lk 9999
```

Submit the job to the master.
```
docker compose exec master /opt/spark/bin/spark-submit --master spark://master:7077 /opt/spark/work-dir/stream.py
```



## Task 1

```(python)
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

spark = SparkSession.builder \
    .appName("SimpleStructuredStreaming") \
    .getOrCreate()
    
def name_sandwich(string):
    return "wilmer" + string + "hallinjakobsson"

# register udf
sandwich_udf = udf(name_sandwich, StringType())
    
inputStream = spark.readStream \
    .format("socket") \
    .option("host", "localhost") \
    .option("port", 9999) \
    .load()

# Use the UDF
sandwichStream = inputStream.select(sandwich_udf(inputStream.value).alias("sandwich"))
sandwiches = sandwichStream.groupBy("sandwich").count()

query = sandwiches\
    .writeStream \
    .outputMode("complete") \
    .format("console") \
    .option("truncate", "false") \
    .start()

query.awaitTermination()
```

## Task 2
```(python)
from pyspark.sql import SparkSession


spark = SparkSession.builder \
    .appName("SimpleStructuredStreaming") \
    .getOrCreate()

    
inputStream = spark.readStream \
    .format("socket") \
    .option("host", "localhost") \
    .option("port", 9999) \
    .load()

lineLengths = inputStream.selectExpr("length(value) as line_length")
avgLength = lineLengths.selectExpr("avg(line_length)")

query = avgLength \
    .writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

query.awaitTermination()
```

## Task 3
```(python)
from pyspark.sql import SparkSession


spark = SparkSession.builder \
    .appName("SimpleStructuredStreaming") \
    .getOrCreate()

    
inputStream = spark.readStream \
    .format("socket") \
    .option("host", "localhost") \
    .option("port", 9999) \
    .load()

inputStream.createOrReplaceTempView("numbers")

evenNumberFilterStream = spark.sql("SELECT value FROM numbers WHERE CAST(value AS INT) % 2 = 0")

evenCounts = evenNumberFilterStream.groupBy("value").count()


query = evenCounts \
    .writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

query.awaitTermination()
```


## Task 4
```(python)
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split


spark = SparkSession.builder \
    .appName("SimpleStructuredStreaming") \
    .getOrCreate()
    
streamingInputDF = spark.readStream \
    .format("socket") \
    .option("host", "localhost") \
    .option("port", 9999) \
    .load()

splitDF = streamingInputDF.selectExpr("split(value, ',')[0] as product", "split(value, ',')[1] as quantity")
splitDF.createOrReplaceTempView("product_sales")
salesPerProduct = spark.sql("SELECT product, SUM(CAST(quantity AS INT)) as total_sales FROM product_sales GROUP BY product")

query = salesPerProduct \
    .writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

query.awaitTermination()
```