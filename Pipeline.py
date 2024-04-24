from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession, SQLContext

import os
driver = os.path.join("lib","postgresql-42.7.3.jar") 
conf = SparkConf() \
    .setAppName("Reyn") \
    .setMaster("local") \
    .set("spark.driver.extraClassPath",driver)

sc = SparkContext.getOrCreate(conf=conf)
spark = SparkSession(sc)
df=spark.read.options(delimiter=",", header=True).csv("data\markets_data.csv")

df.createOrReplaceTempView("market")



dest_tbl = 'public."Mart_table"'
database = "Pipeline"
password = "reyn"
user = "postgres"
#persist

df.write.mode("overwrite") \
    .format("jdbc") \
    .option("url", f"jdbc:postgresql://localhost:5432/{database}") \
    .option("dbtable", dest_tbl) \
    .option("user", user) \
    .option("password", password) \
    .option("driver",  "org.postgresql.Driver") \
    .save()