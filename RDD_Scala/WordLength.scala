import org.apache.spark.SparkContext
import org.apache.spark.SparkConf

val conf = new SparkConf().setAppName("WordLength").setMaster("local")
val sc = new SparkContext(conf)

val text = sc.textFile("C:/Spark/RDD_Scala/Input/WordLength.txt")

val wordLengths = text.flatMap(line => {
    val words = line.split(" ")
    words.map(word => {
        val length = word.length
        val category = length match {
            case 1 => "tiny"
            case x if x >= 1 && x <= 4 => "small"
            case x if x >= 5 && x <= 9 => "medium"
            case _ => "big"
        }
        (word, category)
    })
})

// Sắp xếp kết quả theo key (từ) theo thứ tự từ điển
val sortedCounts = wordLengths.sortByKey()
sortedCounts.saveAsTextFile("C:/Spark/RDD_Scala/Output/WordLength")
sortedCounts.foreach { case (word, category) =>
  println(s"$word: $category")}
sc.stop()
