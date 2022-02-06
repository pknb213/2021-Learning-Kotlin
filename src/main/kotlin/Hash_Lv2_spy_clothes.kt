/**
 * 문제 설명
스파이들은 매일 다른 옷을 조합하여 입어 자신을 위장합니다.

예를 들어 스파이가 가진 옷이 아래와 같고 오늘 스파이가 동그란 안경, 긴 코트, 파란색 티셔츠를 입었다면 다음날은 청바지를 추가로 입거나 동그란 안경 대신 검정 선글라스를 착용하거나 해야 합니다.

종류	| 이름
얼굴	동그란 안경, 검정 선글라스
상의	파란색 티셔츠
하의	청바지
겉옷	긴 코트

스파이가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.

제한사항
clothes의 각 행은 [의상의 이름, 의상의 종류]로 이루어져 있습니다.
스파이가 가진 의상의 수는 1개 이상 30개 이하입니다.
같은 이름을 가진 의상은 존재하지 않습니다.
clothes의 모든 원소는 문자열로 이루어져 있습니다.
모든 문자열의 길이는 1 이상 20 이하인 자연수이고 알파벳 소문자 또는 '_' 로만 이루어져 있습니다.
스파이는 하루에 최소 한 개의 의상은 입습니다.

입출력 예
clothes | return
[["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]	5
[["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]	3

풀이
 모자가 3개, 상의가 2개, 바지가 2개일 때를 생각 해보자
 조합할 수 있는 최소는 1개 그리고 최대 3개이다. 한가지만 입는 경우가 최소이고 최대는 동일한 종류의 의상을 입지 못하기 때문에 종류의 수이다.

 1가지 옷을 입을 때 경우의 수는 전체 의상 수이다. 3 + 2 + 2 = 7가지
 2가지 옷을 입을 떄 경우의 수는 모자와 상의 조합 (3 * 2) = 6, 모자와 바지 (3 * 2) = 6, 상의와 바지 (2 * 2) = 4 => 총 16가지
 3가지 옷을 입을 때 경우의 수는 모자, 상의, 바지 조합 (3 * 2 * 2) = 12가지
 총 7 + 16 + 12 = 35가지
 */
class Hash_Lv2_spy_clothes {
    private val clothes: Array<Array<String>> = arrayOf(
        arrayOf("WooYoungMi", "headgear"),
        arrayOf("JunJi", "headgear"),
        arrayOf("SongZiO", "headgear"),
        arrayOf("GentleMonster", "eyewear"),
        arrayOf("GuuGi", "eyewear"),
        arrayOf("Dior", "face"),
        arrayOf("YSL", "face"),
//        arrayOf("smoky_makeup", "face"),
    )
    fun solution(): Any {
        val res =  clothes.groupBy { // 의상 리스트를 그룹화한다.
            it[1] // 의상 리스트 = [0: 이름, 1: 종류] 이므로 종류로 그룹화한다.
            /* 아래 처럼 동일한 종류로 그룹화된다. 종류 = [ 이름 ]
                headgear=[[Ljava.lang.String;@1be6f5c3, [Ljava.lang.String;@6b884d57, [Ljava.lang.String;@6b184d47]
                eyewear=[[Ljava.lang.String;@72ea2f77, [Ljava.lang.String;@6a124d27]
                face=[[Ljava.lang.String;@33c7353a, [Ljava.lang.String;@681a9515]
             */
        }
            .values
            /* values를 이용하여 종류 리스트에서 이름 리스트만 넘겨준다.
                [[Ljava.lang.String;@4c873330, [Ljava.lang.String;@119d7047], [Ljava.lang.String;@100a117]
                [[Ljava.lang.String;@41629346], [Ljava.lang.String;@00201861]
                [[Ljava.lang.String;@404b9385, [Ljava.lang.String;@6d311334]
             */
            .fold(1) { // reduce와 같이 순차적으로 전체 적용하여 누적 값을 반환하는 함수이다. reduce는 초기값이 없고 fold는 초기 값이 있다.
                acc, v ->
//                println("$acc, ${v.size}")
                acc * (v.size + 1)
                /* acc (Accumulates)의 약자로 누적 값과 value를 로컬 파라미터로 받는다.
                   순차적으로 적용하는 계산식은 누적값 * (value 크기 + 1) 이다.
                   1st  acc = 1 (fold 초기 값), v = [headgear 1, headgear 2, headgear 3]
                        1 * (3 + 1) = 4
                   2nd  acc = 3, v = [eyewear 1, eyewear 2]
                        4 * (2 + 1 ) = 12
                   3rd  acc = 6, v = [face 1, face 2]
                        12 * (2 + 1) = 36
                 */
            } - 1  // 36 - 1 => 35
        println(res)
        return res
    }
}