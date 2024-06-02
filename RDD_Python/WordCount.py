import findspark
findspark.init()

from pyspark import SparkConf
from pyspark import SparkContext

conf = SparkConf()
# conf.setMaster('spark://192.168.1.91:7077')
conf.setMaster('local')
conf.setAppName('WordCount')

# Khởi tạo SparkContext
sc = SparkContext(conf=conf)

# Đọc dữ liệu từ một tập tin văn bản
text = sc.textFile("C:/Spark/RDD_Python/Input/WordCount.txt")

# Chia các dòng thành các từ và tạo RDD mới
counts = text.flatMap(lambda line: line.split())\
    .filter(lambda word: len(word) > 0)\
    .map(lambda word: (word, 1))\
    .reduceByKey(lambda a, b: a + b)

# Sắp xếp kết quả theo key
sorted_counts = counts.sortByKey()

# Lưu kết quả ra file văn bản
sorted_counts.saveAsTextFile("C:/Spark/RDD_Python/Output/WordCount")
output = sorted_counts.collect()
for (word, count) in output:
    print("%s: %i" % (word, count))

# Dừng SparkContext
sc.stop()