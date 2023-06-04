from audioop import avg
import datetime

from pyspark import SparkContext
from pyspark.conf import SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql import functions as F


conf = SparkConf()
conf.setMaster("local").setAppName("My app")

sc = SparkContext.getOrCreate(conf=conf)
spark_session = SparkSession(sc)

df_1 = spark_session.createDataFrame(
    data=[
        [datetime.date(2020, 1, 1), 'demo', 1.123, 10],
        [datetime.date(2020, 1, 1), 'demo', 5.286, 10]
    ],
    schema=StructType(
        [
            StructField('col_a', DateType(), True),
            StructField('col_b', StringType(), True),
            StructField('col_c', DoubleType(), True),
            StructField('col_d', LongType(), True),
        ]
    ),
)

df_2 = spark_session.createDataFrame(
    data=[
        [datetime.date(2020, 1, 1), 'demo', 4.321, 10],
        [datetime.date(2020, 1, 1), 'demo', 6.900, 10]
    ],
    schema=StructType(
        [
            StructField('col_a', DateType(), True),
            StructField('col_b', StringType(), True),
            StructField('col_c', DoubleType(), True),
            StructField('col_d', LongType(), True),
        ]
    ),
)

df_1.show()
df_2.show()

df_3 = df_1.join(df_2)
df_3.show()

df_4 = df_1.union(df_2)
df_4.show()

df_5 = df_4.groupBy("col_b").agg(F.min("col_c"),F.max("col_c"),F.avg("col_c"),F.sum("col_c")) # {"col_c":"max"}, {"col_c":"avg"}, {"col_c":"sum"}
df_5.show()