
# Lab 2

Started the master and the worker through Docker's GUI.

```
docker cp /path/to/task_1.py spark-master:/opt/bitnami/spark/
```
![text](./images/task_1/copy_script.png)

```
docker exec -it spark-master /bin/bash
```
![text](./images/task_1/exec_spark-master.png)

```
/opt/bitnami/spark/bin/spark-submit \
  --master spark://spark-master:7077 \
  --conf spark.jars.ivy=/tmp/.ivy2 \
  /opt/bitnami/spark/task_1.py
```
![text](./images/task_1/submit_spark_job.png)


First python code executed showing the created dataframe and the column names with their datatypes.
![text](./images/task_1/first_dataframe.png.png)

Only product and price columns. 
![text](./images/task_1/product_and_price.png)

```
items_df.filter("price > 2").show()
```
![text](./images/task_1/product_and_price.png)

count in each category.
![text](./images/task_1/count_category.png)

Average price.
![text](./images/task_1/avg_price.png)

Sales price.
![text](./images/task_1/sales_price.png)

Create a temp view.
```
items_df.createOrReplaceTempView("retail_sales")
```
Number of sales per product.
![text](./images/task_1/num_of_sales.png)

Sum of sales for each category.
![text](./images/task_1/sum_sales_for_categories.png)


When creating a pandas UDF, I needed to install pandas and pyarrow. (Both in the master and the worker).
```
pip install pandas pyarrow
```
![text](./images/task_2/install_pandas.png)

Copy over the python script for task 2.
![text](./images/task_2/copy_python_script.png)

Submit the script.
![text](./images/task_2/submit.png)

Utilizing the custom Spark UDF that multiplies the numbers in the dataframe by 3.
![text](./images/task_2/spark_udf.png)

Now the Pandas UDF that subtracts two.
![text](./images/task_2/pandas_udf.png)



### Error
There was a '*' sign in the dataset string in the PDF that made the attempt to submit the python script throw an error.



Tip to self: crtl + P followed by ctrl + Q to stop a docker session/execution in terminal. (undo docker exec ...)


