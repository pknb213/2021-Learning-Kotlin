package Programmers

import java.util.*

/**
 * 문제 설명
스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

속한 노래가 많이 재생된 장르를 먼저 수록합니다.
장르 내에서 많이 재생된 노래를 먼저 수록합니다.
장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

제한사항
genres[i]는 고유번호가 i인 노래의 장르입니다.
plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
장르 종류는 100개 미만입니다.
장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
모든 장르는 재생된 횟수가 다릅니다.

입출력 예
genres	plays	return
["classic", "pop", "classic", "classic", "pop"]	[500, 600, 150, 800, 2500]	[4, 1, 3, 0]

입출력 예 설명
classic 장르는 1,450회 재생되었으며, classic 노래는 다음과 같습니다.
고유 번호 3: 800회 재생
고유 번호 0: 500회 재생
고유 번호 2: 150회 재생

pop 장르는 3,100회 재생되었으며, pop 노래는 다음과 같습니다.
고유 번호 4: 2,500회 재생
고유 번호 1: 600회 재생
따라서 pop 장르의 [4, 1]번 노래를 먼저, classic 장르의 [3, 0]번 노래를 그 다음에 수록 합니다.

풀이
 예시를 자세히 생각 해보자.
 
 */
class Hash_Lv3_best_album {
    private val genres = listOf<String>("classic", "pop", "classic", "classic", "pop", "ani", "Kpop", "Kpop")
    private val plays = listOf<Int>(500, 600, 150, 800, 2500, 1350, 500, 500)

    fun solution(): IntArray {
        return genres.indices.groupBy {
            /**
                indices로 genres의 index range를 구하여 groupBy에 Key 값으로 전달 한다.
                그러면 genres Key 값으로 일치 하는 element index를 value로 저장 한다.
                -> map(classic, [0, 2, 3])  아래 toList 수행 후 까지.
             */
            genres[it]
        }
            .toList()
            .map { println(it); it }
            .sortedByDescending {
                /**
                 * 많이 재생된 순으로 정렬을 하고자 한다.
                 * 그래서 second로 고유 번호 리스트에 접근하여 sumOf을 사용하여 실행 된 합을 구하고 해당 값으로
                 * sortedByDescending 내림 차순 정렬 한다.
                 */
                genresIndexList -> val sumOfPlays = genresIndexList.second.sumOf { plays[it] }
                val totalPlaySet = mutableSetOf(genresIndexList.first to sumOfPlays).toSet().distinct() // 중복 제거가 안되넹
                sumOfPlays
//                it.second.sumBy { plays[it] }
            }
            .map{ println(it); it } // 많이 실행 된 순
            .map {
                /**
                 * 고유 번호가 작은 낮은 노래 순으로 2개를 반환하도록 한다.
                 * 내림차순 재생 순서로 가장 많이 실행된 노래를 take 명령어로 2개 반환 한다.
                 */
                it.second.sortedByDescending { plays[it] }.take(2)
            }
            .map{ println(it); it }
            .flatten() /** flatten 명령어로 List<List<>> 형태의 리스트들을 하나로 만든다.*/
            .map{println(it); it}
            .toIntArray() /** 결과값이 IntArray이기 때문에*/
    }
}