# Big Data Essentials
Đồ án môn học Nhập môn dữ liệu lớn - BDES333877_23_2_03CLC, trường Đại học Sư phạm Kỹ thuật Thành phố Hồ Chí Minh

Môn học Nhập môn dữ liệu lớn tìm hiểu và cài đặt về:
- Hadoop Cluster
- Hadoop Streaming
- Hadoop MapReduce
## Đề tài
Tìm hiểu và cài đặt các bài MapReduce trên Apache Spark
## Mục tiêu đề tài
- Hiểu rõ về mô hình lập trình MapReduce và cách thức hoạt động của nó trong Apache Spark. 
- Cài đặt và cấu hình môi trường Spark để thực hành các bài MapReduce. 
- Viết các chương trình Spark bằng Scala hoặc Python để thực hiện các bài toán MapReduce cơ bản như đếm từ, tính tổng, tìm giá trị trung bình,…
- Đề tài này thực hiện chủ yếu các lý thuyết cơ bản về Apache Spark, cài đặt Apache Spark, thiết lập cụm Spark Cluster Master Slave và cài đặt các chương trình của Apache Spark như SparkSQL, Spark Streaming, các bài toán MapReduce trong Spark.
## Công nghệ
- Ngôn ngữ: Python, Scala
- IDE: Visual Studio Code
## Demo các bài Map Reduce
### WordCount
Mục tiêu của bài này là đếm số lần xuất hiện mỗi từ trong tập input đầu vào, ví dụ từ “It” xuất hiện bao nhiêu lần, từ “is” xuất hiện bao nhiêu lần,…

Output: Từ và số lần xuất hiện của từ đó

![image](https://github.com/ThuyQuynh2407/BigData/assets/171242217/6eaefba1-2d4d-4911-93f2-7e8bce76535c)

### WordLength
Mục tiêu của bài này là đếm số lần xuất hiện mỗi loại từ “small”, “tiny”, “medium”, “big” xuất hiện bao nhiêu lần

![image](https://github.com/ThuyQuynh2407/BigData/assets/171242217/aa93ef8b-e16f-46a8-808f-793d7cdb5d88)

### FriendCount
Mục tiêu của bài này là đếm số lượng bạn bè của mỗi người, output sẽ in ra tên của một người và số lượng bạn bè của người đó là bao nhiêu

![image](https://github.com/ThuyQuynh2407/BigData/assets/171242217/53a1bd1e-2927-44cb-b944-4c3a7cde9b4f)

### Comprehension
Tập input là thư mực Comprehension chứa 2 file txt là Comprehension1.txt và Comprehension2.txt

Mục đích của bài này là cho biết từ đó thuộc file nào

Output: Hiện ta từ đó và file mà có chứa từ đó
![image](https://github.com/ThuyQuynh2407/BigData/assets/171242217/392a4b1d-09a0-4861-b607-1466768bd73a)
