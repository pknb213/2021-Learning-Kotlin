fun main() {
    // is 연산자는 인스턴트의 타입 표현식을 체크합니다. 만약 불변적인 지역 변수 또는 프로퍼티는
    fun getStringLength(obj: Any): Int?{
        if (obj is String) {
            // obj is String일 경우 String으로 자동 형 변환이 됩니다.
            return obj.length
        }
        // obj는 여전히 Any 타입 일 경우 수행.
        return null
    }

    // Or
    fun getStringLength2(obj: Any): Int? {
        if (obj !is String) return null
        // obj !is String가 아닌 경우 String으로 자동 형 변환이 됩니다.
        return null
    }
    // Or even
    fun getStringLength3(obj: Any): Int? {
        // `obj`는 &&의 오른쪽에 있는 String으로 자동 형 변환이됩니다.
        if (obj is String && obj.length > 0) {
            return obj.length
        }
        return null
    }
    println(getStringLength("Hello"))
    println(getStringLength2("Hi"))
    println(getStringLength3("Welcome"))
}