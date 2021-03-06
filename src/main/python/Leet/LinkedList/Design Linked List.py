"""
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node,
and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list.
Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list.
After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list.
If index equals the length of the linked list, the node will be appended to the end of the linked list.
If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.

Example 1:
    Input
    ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
    [[], [1], [3], [1, 2], [1], [1], [1]]

    Output
    [null, null, null, null, 2, null, 3]

Explanation
    MyLinkedList myLinkedList = new MyLinkedList();
    myLinkedList.addAtHead(1);
    myLinkedList.addAtTail(3);
    myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
    myLinkedList.get(1);              // return 2
    myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
    myLinkedList.get(1);              // return 3

Constraints:
    0 <= index, val <= 1000
    Please do not use the built-in LinkedList library.
    At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.
"""
class MyLinkedList_Fail:

    def __init__(self):
        self.node = []

    def get(self, index: int) -> int:
        if len(self.node) == 0:
            return "Null"
        return self.node.pop(index)

    def addAtHead(self, val: int) -> None:
        if len(self.node) == 0:
            self.node.append(val)
        else:
            self.node.insert(0, val)

    def addAtTail(self, val: int) -> None:
        self.node.insert(-1, val)

    def addAtIndex(self, index: int, val: int) -> None:
        self.node.insert(index, val)

    def deleteAtIndex(self, index: int) -> None:
        self.node.pop(index)


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def show_all(self):
        print("\n--- Show All ---")
        current = self.head  # ?????? 1?????? ?????????, ?????? ????????? ?????? ????????? ??????

        if self.size <= 0:
            print("Empty\n")
            return
        for i in range(self.size):
            print("Val:", current.val)
            current = current.next
        print("\n")

    def get(self, index: int) -> int:
        print("GET: ", index)
        if index < 0 or index >= self.size:  # ?????? ?????????, ????????? ????????? index??? ??? ??????
            return -1

        current = self.head

        for i in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        print("Add Head {}".format(val))
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        print(f"Add Tail {val}")
        # self.addAtIndex(-1, val)
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        print("Add Index [{0}] = {1}".format(index, val))
        if index > self.size:  # ????????? ????????? index??? ??? ??????
            return

        current = self.head   # ?????? prev??? next??? curr head??? ???????????? None
        newNode = Node(val)   # ?????? ?????? ?????? (none, val)s

        if index <= 0:  # ????????? ???????????? ?????? ?????? ??????
            newNode.next = current  # ????????? ?????? ????????? next??? ?????? ?????? curr??? None??? ??????
            self.head = newNode  # ?????????, ????????? ????????? head??? ?????? ????????? ??????   | 3 | None |  ?????? ??????
        else:
            for i in range(index - 1):  # ????????? ????????? index ?????? ?????? ??????
                current = current.next
            newNode.next = current.next  # ?????? ???, ????????? ????????? next ??????
            current.next = newNode      # ?????? ?????? next??? ????????? ?????? ??????

        self.size += 1  # ?????? ?????? ??????

    def deleteAtIndex(self, index: int) -> None:
        print(f"Del Index [{index}]")
        if index >= self.size:
            return

        current = self.head

        if index == 0:
            self.head = current.next
        else:
            for i in range(0, index - 1):
                current = current.next
            current.next = current.next.next

        self.size -= 1  # ?????? ?????? ??????


p1 = ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
p2 = [[], [1], [3], [1, 2], [1], [1], [1]]
# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
param_1 = obj.get(1)
obj.show_all()
obj.addAtHead(1)
obj.show_all()
obj.addAtTail(3)
obj.show_all()
obj.addAtIndex(1,2)
obj.show_all()
obj.deleteAtIndex(2)
obj.show_all()