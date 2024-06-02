import findspark
findspark.init()

from pyspark import SparkConf, SparkContext

# Khởi tạo SparkConf
conf = SparkConf()
#conf.setMaster('spark://192.168.1.91:7077')
#conf.setMaster('local')
conf.setAppName("WordLength")

# Khởi tạo SparkContext
sc = SparkContext(conf=conf)

# Đọc dữ liệu từ tệp văn bản
text = sc.textFile("C:/Spark/RDD_Python/Input/WordLength.txt")

# Hàm phân loại từ thành phân loại tương ứng
def categorize_word(word):
    length = len(word)
    if length == 1:
        return "tiny"
    elif 1 < length <= 4:
        return "small"
    elif 5 <= length <= 9:
        return "medium"
    else:
        return "big"

# Tạo RDD mới để đếm số lượng từ trong mỗi phân loại
category_counts = text.flatMap(lambda line: line.split()) \
                      .map(lambda word: (categorize_word(word), 1)) \
                      .reduceByKey(lambda a, b: a + b)

# Lưu kết quả vào file văn bản
sorted_counts=category_counts.saveAsTextFile("C:/Spark/RDD_Python/Output/WordLength")
output = sorted_counts.collect()
for (word, count) in output:
    print("%s: %i" % (word, count))


# Dừng SparkContext
sc.stop()