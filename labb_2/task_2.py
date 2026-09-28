from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType
from pyspark.sql.functions import udf, pandas_udf
import pandas as pd
import pyspark.sql.functions as sf

if __name__ == "__main__":
    spark = SparkSession.builder.appName("UDFTransformation").getOrCreate()
    
    def multiply_by_three(number:int) -> int:
        return number * 3
    
    multiply_by_three_udf = udf(multiply_by_three, IntegerType())
    
    df = spark.createDataFrame([(t,) for t in [4,5,6]],["number"])
    
    #df.select(multiply_by_three_udf("number").alias("multiplied_by_three")).show()
    df.withColumn("multiplied_by_three", multiply_by_three_udf("number")).show()
    
    @pandas_udf(IntegerType())
    def minus_two_pd_udf(number: pd.Series) -> pd.Series:
        return number - 2
    
    df.withColumn("minus_two_pd", minus_two_pd_udf("number")).show()