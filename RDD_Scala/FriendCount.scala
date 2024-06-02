import org.apache.spark.SparkContext
import org.apache.spark.SparkConf

val conf = new SparkConf().setAppName("FriendCount").setMaster("local")
//val conf = new SparkConf().setAppName("FriendCount").setMaster("spark://192.168.167.148:7077")
val sc = new SparkContext(conf)

val text = sc.textFile("C:/Spark/RDD_Scala/Input/FriendCount.txt")
val counts = text.flatMap(line => line.split(" ")).map(word => (word, 1)).reduceByKey(_ + _)

// Sắp xếp kết quả theo key (từ) theo thứ tự từ điển
val sortedCounts = counts.sortByKey()

sortedCounts.saveAsTextFile("C:/Spark/RDD_Scala/Output/FriendCount")

// Lặp qua kết quả và in ra từng cặp (person, count)
sortedCounts.foreach { case (person, count) =>
  println(s"$person: $count")
}

sc.stop()
