import findspark
findspark.init()

from pyspark import SparkConf
from pyspark import SparkContext
import os

conf = SparkConf()
#conf.setMaster('spark://192.168.1.91:7077')
conf.setMaster('local')
conf.setAppName('Comprehension')

# Khởi tạo SparkContext
sc = SparkContext(conf=conf)

# Đọc dữ liệu từ các tệp văn bản vào RDD
text_rdd = sc.wholeTextFiles("C:/Spark/RDD_Python/Input/Comprehension/*")

# Trích xuất tên tệp từ đường dẫn đầy đủ
def extract_file_name(file_path):
    return os.path.basename(file_path)

# Define the tokenizer function
def tokenize(file_name, text):
    words = text.split()
    return [(word, file_name) for word in set(words)]  # Sử dụng set để chỉ gán một lần cho mỗi từ

# Tokenize each file
tokenized_rdd = text_rdd.flatMap(lambda file: tokenize(extract_file_name(file[0]), file[1]))

# Group by word
grouped_rdd = tokenized_rdd.groupByKey()

# Concatenate file names
result_rdd = grouped_rdd.mapValues(lambda values: "|".join(values))

#
sorted_rdd = result_rdd.sortByKey()

# Lưu kết quả ra file văn bản
sorted_rdd.saveAsTextFile("C:/Spark/RDD_Python/Output/Comprehension")

# In ra kết quả trên terminal
output = sorted_rdd.collect()
for (word, files) in output:
    print(f"{word}: {files}")

# Dừng SparkContext
sc.stop()
