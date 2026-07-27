class DoublyLinkedList:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.head = DoublyLinkedList(-1)
        self.tail = DoublyLinkedList(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        node = DoublyLinkedList(value)
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        self.tail.prev = node
        node.next = self.tail
        self.capacity -= 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        self.capacity += 1
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.head.next.val

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.tail.prev.val

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def isFull(self) -> bool:
        return self.capacity == 0


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()