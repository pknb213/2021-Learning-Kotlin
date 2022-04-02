package Programmers

/**
 일반적인 프린터는 인쇄 요청이 들어온 순서대로 인쇄합니다. 그렇기 때문에 중요한 문서가 나중에 인쇄될 수 있습니다.
 이런 문제를 보완하기 위해 중요도가 높은 문서를 먼저 인쇄하는 프린터를 개발했습니다. 이 새롭게 개발한 프린터는 아래와 같은 방식으로 인쇄 작업을 수행합니다.

1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
3. 그렇지 않으면 J를 인쇄합니다.
예를 들어, 4개의 문서(A, B, C, D)가 순서대로 인쇄 대기목록에 있고 중요도가 2 1 3 2 라면 C D A B 순으로 인쇄하게 됩니다.

내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 알고 싶습니다. 위의 예에서 C는 1번째로, A는 3번째로 인쇄됩니다.

현재 대기목록에 있는 문서의 중요도가 순서대로 담긴 배열 priorities와 내가 인쇄를 요청한 문서가 현재 대기목록의 어떤 위치에 있는지를 알려주는 location이 매개변수로 주어질 때,
 내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 return 하도록 solution 함수를 작성해주세요.

 제한사항
 현재 대기목록에는 1개 이상 100개 이하의 문서가 있습니다.
 인쇄 작업의 중요도는 1~9로 표현하며 숫자가 클수록 중요하다는 뜻입니다.
 location은 0 이상 (현재 대기목록에 있는 작업 수 - 1) 이하의 값을 가지며 대기목록의 가장 앞에 있으면 0, 두 번째에 있으면 1로 표현합니다.
 입출력 예
 priorities	location	return
 [2, 1, 3, 2]	2	1
 [1, 1, 9, 1, 1, 1]	0	5

 입출력 예 설명
 예제 #2 : 6개의 문서(A, B, C, D, E, F)가 인쇄 대기목록에 있고 중요도가 1 1 9 1 1 1 이므로 C D E F A B 순으로 인쇄합니다.
 */
import java.util.Queue
import java.util.LinkedList
import java.util.Stack

class StackQueue_Lv2_Printer {
    private val priorities: IntArray = listOf(1,1,9,1,1,1).toIntArray()
    private val location: Int = 0
    lateinit var queue: Queue<Int>
    lateinit var stack: Stack<Int>
    lateinit var q2: Queue<Char>
    lateinit var s2: Stack<Char>
    fun solution(): Int{
        println(listOf(1,1,1).maxOrNull())
        queue = LinkedList()
        queue.addAll(priorities.toList())
        stack = Stack()
        q2 = LinkedList()
        s2 = Stack()
        q2.addAll(CharRange('A',priorities.size.plus(64).toChar()).toList())
        val searchValue = q2.elementAt(location)
        while (queue.isNotEmpty()){
            println("Poll > ${queue.peek()}")
            val item = queue.poll()
            println("Max > ${queue.maxOrNull()}")
            queue.maxOrNull()?.let {
                if (item < it) {
                    queue.add(item)
                    q2.add(q2.poll())
                }else{
                    stack.push(item)
                    s2.push(q2.poll())
                }
            }?: run {
                stack.push(item)
                s2.push(q2.poll())
            }
            println("Queue > $queue\nStack > $stack")
        }
        println("q2 > $q2\ns2 > $s2")
        return s2.indexOf(searchValue)+1
    }
}

/** 참고할 풀이 (deque 사용)
var printerQueue = ArrayDeque<Pair<Int,Int>>()
priorities.forEachIndexed{index, i ->
printerQueue.offer(Pair(index,i))
}

var count = 0
while (!printerQueue.isEmpty()){
var first = printerQueue.poll()

if(printerQueue.filter { first.second < it.second }.size > 0){
printerQueue.offer(first)
}else{
count++
if(first.first == location) return count
}
}
return 0
 */