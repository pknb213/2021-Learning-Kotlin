fun main() {
    val items = listOf("a", "b", "C")
    // for
    for (item in items) {
        println(item)
    }
    // for 2
    for (index in items.indices) {
        println("item at $index is ${items[index]}")  // Return 0, a
    }
    // while
    var index = 0
    while (index < items.size) {
        println("$index, ${items[index]}")
        index++
    }
}