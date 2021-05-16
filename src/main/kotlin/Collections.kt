@ExperimentalStdlibApi
fun main() {
    val items = listOf("Ani", "Battle", "Ciba")
    for (item in items)
        println(item)
    when {
        "Ani" in items -> println("Daisuky")
        "Siba" in items -> println("Siba is bad word")
    }

    val fruits = listOf("banana", "apple", "melon", "avocado", "jamong")
    fruits
        .filter { it.startsWith("a") }
        .sortedBy { it }
        .map { it.uppercase() }
        .forEach { println(it) }
}