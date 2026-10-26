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
