from pyspark.sql import SparkSession
import pyspark.sql.functions as sf

if __name__ == "__main__":
  # Initialize a Spark session
  spark = SparkSession.builder.appName("Spark Store Dataframe").getOrCreate()
  # Create a DataFrame from a list of numbers
  items_list = [
        ('Moby Dick', 'Book', 13.75, 11),
        ('Mango', 'Fruit', 3.95, 17),
        ('Ulysses', 'Book', 24.30, 6),
        ('Banana', 'Fruit', 1.70, 30),
        ('Hamlet', 'Book', 19.10, 14),
        ('Orange', 'Fruit', 2.85, 21),
        ('Jane Eyre', 'Book', 21.25, 7),
        ('Strawberry', 'Fruit', 1.75, 28),
        ('1984', 'Book', 17.40, 16),
        ('Watermelon', 'Fruit', 3.45, 10),
        ('Pride and Prejudice', 'Book', 8.75, 18),
        ('Grapes', 'Fruit', 2.45, 23),
        ('To Kill a Mockingbird', 'Book', 20.60, 13),
        ('Peach', 'Fruit', 3.15, 8),
        ('War and Peace', 'Book', 21.80, 12),
        ('Apple', 'Fruit', 2.65, 15),
        ('The Great Gatsby', 'Book', 11.95, 17),
        ('Pineapple', 'Fruit', 3.25, 4),
        ('Don Quixote', 'Book', 20.10, 9),
        ('Moby Dick', 'Book', 6.25, 19),
        ('Banana', 'Fruit', 1.95, 26),
        ('Mango', 'Fruit', 4.50, 12),
        ('Ulysses', 'Book', 22.75, 10),
        ('Orange', 'Fruit', 3.40, 14),
        ('Hamlet', 'Book', 16.85, 18),
        ('Strawberry', 'Fruit', 2.25, 20),
        ('Jane Eyre', 'Book', 18.60, 15),
        ('Watermelon', 'Fruit', 2.95, 13),
        ('1984', 'Book', 18.20, 8),
        ('Grapes', 'Fruit', 2.90, 16),
        ('To Kill a Mockingbird', 'Book', 23.50, 10),
        ('Apple', 'Fruit', 2.75, 19),
        ('Pride and Prejudice', 'Book', 11.40, 14),
        ('Peach', 'Fruit', 2.95, 22),
        ('War and Peace', 'Book', 24.20, 7),
        ('Banana', 'Fruit', 1.60, 35),
        ('The Great Gatsby', 'Book', 14.10, 12),
        ('Pineapple', 'Fruit', 3.05, 9),
        ('Don Quixote', 'Book', 21.30, 11),
        ('Moby Dick', 'Book', 12.90, 16),
        ('Mango', 'Fruit', 4.75, 8),
        ('Ulysses', 'Book', 20.85, 13),
        ('Orange', 'Fruit', 3.15, 25),
        ('Hamlet', 'Book', 18.75, 9),
        ('Strawberry', 'Fruit', 2.05, 32),
        ('Jane Eyre', 'Book', 22.10, 6),
        ('Watermelon', 'Fruit', 3.60, 11),
        ('1984', 'Book', 16.20, 20),
        ('Grapes', 'Fruit', 2.70, 27),
        ('To Kill a Mockingbird', 'Book', 19.95, 15),
        ('Apple', 'Fruit', 2.48, 21),
        ('Pride and Prejudice', 'Book', 12.15, 10),
        ('Peach', 'Fruit', 3.30, 13),
        ('War and Peace', 'Book', 20.95, 14),
        ('The Great Gatsby', 'Book', 13.25, 18)
  ]
  items_df = spark.createDataFrame([(a,b,c,d) for (a,b,c,d) in items_list], ['product_name', 'category', 'price', 'quantity'])
  # Show the DataFrame
  items_df.show()
  print(items_df.schema)
  
  print("--- 4. Data anaylsis --- \n")
  items_df.select(["product_name","price"]).show()
  
  items_df.filter("price > 2").show()
  
  items_df.groupBy("category").count().show()
  
  items_df.select(sf.avg("price")).show()
  
  item_df_with_sale = items_df.withColumn("sale_price", sf.col("price")*0.9)
  item_df_with_sale.show()
  
  # SQL Operations
  items_df.createOrReplaceTempView("retail_sales")
  
  df2 = spark.sql("SELECT product_name, SUM(quantity) FROM retail_sales GROUP BY product_name")
  df2.show()
  
  df3 = spark.sql("SELECT category, SUM(price) FROM retail_sales GROUP BY category")
  df3.show()
  
  
  
  spark.catalog.dropTempView("retail_sales")
  
  # Stop the Spark session
  spark.stop()
  
  
  