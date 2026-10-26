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