import java.lang.Integer.parseInt

fun main() {
    // null 값이 기능할 떄 참조는 명시적으로 nullable로 표시되어야 합니다.
    // Nulable 형식 이름은 뒤에 ? 붙이면 됩니다.
//    fun parseInt(str: String): Int? {
//    }

    fun printProduct(arg1: String, arg2: String){
        val x = parseInt(arg1)
        val y = parseInt(arg2)

        //
        if (x != null && y != null){
            //
            println( x * y )
        } else {
            println("$arg1 or $arg2 is not a number")
        }
        // Or
        if (x == null){
            println("Wrong number format in arg1: $arg1")
            return
        }
        if (y == null){
            println("Wrong number format in arg2: $arg2")
            return
        }
    }
    println(printProduct("7", "10"))
}