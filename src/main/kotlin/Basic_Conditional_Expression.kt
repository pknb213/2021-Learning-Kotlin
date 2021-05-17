fun main() {
    fun maxOf(a: Int, b: Int): Int {
        return if (a > b) {
            a
        } else {
            b
        }
    }
    // Use expression
    fun maxOf2(a: Int, b: Int) = if (a > b) a else b

    println(maxOf(4, 8))
    println(maxOf2(4, 8))
}