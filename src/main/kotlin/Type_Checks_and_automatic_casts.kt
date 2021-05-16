fun main() {
    // is 연산자는 인스턴트의 타입 표현식을 체크합니다. 만약 불변적인 지역 변수 또는 프로퍼티는
    fun getStringLength(obj: Any): Int?{
        if (obj is String) {
            // `obj` is automatically cast to `String` in this branch
            return obj.length
        }
        // `obj` is still of type `Any` outside of the type-checked branch
        return null
    }

    // Or
    fun getStringLength2(obj: Any): Int? {
        if (obj !is String) return null
        // `obj` is automatically cast to `String` in this bran
        return null
    }
    // Or even
    fun getStringLength3(obj: Any): Int? {
        // `obj` is automatically cast to `String` on the right-hand side of `&&`
        if (obj is String && obj.length > 0) {
            return obj.length
        }
        return null
    }
}