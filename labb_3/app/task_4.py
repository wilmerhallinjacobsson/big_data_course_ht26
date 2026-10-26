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