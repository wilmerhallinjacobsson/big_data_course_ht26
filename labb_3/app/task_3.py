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