class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and cur != self.right and index == 0:
            return cur.val
        return -1

    def addAtHead(self, val: int) -> None:
        cur = self.left.next
        new_head = ListNode(val)
        cur.prev = new_head
        self.left.next = new_head
        new_head.prev = self.left
        new_head.next = cur

    def addAtTail(self, val: int) -> None:
        cur = self.right.prev
        new_tail = ListNode(val)
        cur.next = new_tail
        self.right.prev = new_tail
        new_tail.prev = cur
        new_tail.next = self.right

    def addAtIndex(self, index: int, val: int) -> None:
        node = ListNode(val)
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and index == 0:
            prev = cur.prev
            prev.next = node
            cur.prev = node
            node.next = cur
            node.prev = prev

    def deleteAtIndex(self, index: int) -> None:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and cur != self.right and index == 0:
            next, prev = cur.next, cur.prev
            prev.next = next
            next.prev = prev