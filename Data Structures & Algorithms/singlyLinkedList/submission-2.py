class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def get(self, index: int) -> int:
        cur = self.head
        while cur and index>0:
            cur = cur.next
            index-=1
        if cur and index == 0:
            return cur.val
        return -1

    def insertHead(self, val: int) -> None:
        node = ListNode(val)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            tmp = self.head
            self.head = node
            node.next = tmp
        self.size+=1

    def insertTail(self, val: int) -> None:
        node = ListNode(val)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            tmp = self.tail
            tmp.next = node
            self.tail = node
            self.tail.next = None
        self.size+=1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return False
        if index == 0:
            self.head = self.head.next
            if self.size == 1:
                self.tail = None
            self.size -= 1
            return True
        cur = self.head
        for _ in range(index - 1):
            cur = cur.next
        if cur.next == self.tail:
            self.tail = cur
        cur.next = cur.next.next
        self.size -= 1
        return True

    def getValues(self) -> List[int]:
        cur = self.head
        lst = []
        while cur:
            lst.append(cur.val)
            cur = cur.next
        return lst