import findspark
findspark.init()

from pyspark import SparkConf
from pyspark import SparkContext

conf = SparkConf()
# conf.setMaster('spark://192.168.1.91:7077')
conf.setMaster('local')
conf.setAppName('FriendCount')

# Khởi tạo SparkContext
sc = SparkContext(conf=conf)

# Đọc dữ liệu từ một tập tin văn bản chứa danh sách bạn bè
friend_list = sc.textFile("C:/Spark/RDD_Python/Input/FriendCount.txt")

# Chia các dòng thành các cặp bạn bè và tạo RDD mới
friend_pairs = friend_list.flatMap(lambda line: line.split(",")).map(lambda pair: (pair.split()[0], 1))

# Tính tổng số bạn của mỗi người
friend_counts = friend_pairs.reduceByKey(lambda a, b: a + b)

# Sắp xếp kết quả theo key
sorted_counts = friend_counts.sortByKey()

# Lưu kết quả ra file văn bản
sorted_counts.saveAsTextFile("C:/Spark/RDD_Python/Output/FriendCount")
output = sorted_counts.collect()
for (person, count) in output:
    print("%s: %i" % (person, count))

# Dừng SparkContext
sc.stop()
