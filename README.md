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

![Screenshot 2024-06-02 130610](https://github.com/ThuyQuynh2407/BigDataEssentials/assets/171242217/45ec6ca7-9e7a-4363-a682-8c861859dec8)

### WordLength
Mục tiêu của bài này là đếm số lần xuất hiện mỗi loại từ “small”, “tiny”, “medium”, “big” xuất hiện bao nhiêu lần

![Screenshot 2024-06-02 130435](https://github.com/ThuyQuynh2407/BigDataEssentials/assets/171242217/5a885dfb-3562-4a1e-8638-4b061c763e0a)

### FriendCount
Mục tiêu của bài này là đếm số lượng bạn bè của mỗi người, output sẽ in ra tên của một người và số lượng bạn bè của người đó là bao nhiêu

![Screenshot 2024-06-02 130315](https://github.com/ThuyQuynh2407/BigDataEssentials/assets/171242217/3b47b781-83e1-487b-8719-a2b109065df2)

### Comprehension
Tập input là thư mực Comprehension chứa 2 file txt là Comprehension1.txt và Comprehension2.txt

Mục đích của bài này là cho biết từ đó thuộc file nào

Output: Hiện ta từ đó và file mà có chứa từ đó

![Screenshot 2024-06-02 130640](https://github.com/ThuyQuynh2407/BigDataEssentials/assets/171242217/ff96e103-e4d2-4100-a34d-bf9b905a11c6)
