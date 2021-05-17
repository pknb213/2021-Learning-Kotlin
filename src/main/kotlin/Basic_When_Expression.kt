fun main() {
    fun describe(obj: Any): String =
        when (obj){
            1           ->  "One"
            "Hello"     ->  "Greeting"
            is Long     ->  "Long"
            !is String  ->  "Not a string"
            else        ->  "Unknown"
        }
    println(describe(0))
}