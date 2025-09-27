from pyspark.sql import SparkSession
# Create a Spark session
spark = SparkSession.builder.getOrCreate()
# Read OSINT data into a Spark DataFrame
data = spark.read.csv('osint_data.csv', header=True)
# Perform data manipulation and analysis using Spark SQL or DataFrame API
# Example: Calculate the count of records for each category
data.groupBy('Category').count().show()
