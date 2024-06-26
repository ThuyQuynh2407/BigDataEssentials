from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Create the SparkSession
spark = SparkSession.\
builder.\
appName("sparkstream").\
getOrCreate()

# Define input sources
lines = (spark\
.readStream.format("socket")\
#.option("host", "192.168.1.133")\
.option("host", "localhost")\
.option("port", 9999)\
.load())

# Transform data
words = lines.select(explode(split(col("value"), " ")).alias("word"))

# Get the count of published words
counts = words.groupBy("word").count()

# Define the checkpoint directory
checkpointDir = "C:/Spark/Spark_Python/Output/Streaming"

# Start streaming defining the necessary configurations
streamingQuery = (counts
.writeStream
.format("console")
.outputMode("complete")
.trigger(processingTime="1 second")
.option("checkpointLocation", checkpointDir)
.start())
streamingQuery.awaitTermination()