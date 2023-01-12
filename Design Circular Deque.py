# https://leetcode.com/problems/design-circular-deque/description/
# https://leetcode.com/problems/design-circular-deque/solutions/154055/python3-using-list-easy-to-understand/

class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.front = 0
        self.rear = 0
        self.size = 0
        self.data = [-1] * k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.size == 0:
            self.data[self.front] = value
        else:
            self.front = (self.front - 1) % self.k
            self.data[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.size == 0:
            self.data[self.rear] = value
        else:
            self.rear = (self.rear + 1) % self.k
            self.data[self.rear] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.data[self.front] = -1
        self.front = (self.front + 1) % self.k
        self.size -= 1
        if self.isEmpty():
            self.rear = self.front
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.data[self.rear] = -1
        self.rear = (self.rear - 1) % self.k
        self.size -= 1
        if self.isEmpty():
            self.front = self.rear
        return True

    def getFront(self) -> int:
        return self.data[self.front]

    def getRear(self) -> int:
        return self.data[self.rear]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


# concise
class MyCircularDeque2:

    def __init__(self, k: int):
        self.k = k
        self.front = 0
        self.rear = 0
        self.size = 0
        self.data = [-1] * k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if not self.isEmpty():
            self.front = (self.front - 1) % self.k
        self.data[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if not self.isEmpty():
            self.rear = (self.rear + 1) % self.k
        self.data[self.rear] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.data[self.front] = -1
        self.size -= 1
        self.front = ((self.front + 1) % self.k) if not self.isEmpty() else self.front
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.data[self.rear] = -1
        self.size -= 1
        self.rear = ((self.rear - 1) % self.k) if not self.isEmpty() else self.rear
        return True

    def getFront(self) -> int:
        return self.data[self.front]

    def getRear(self) -> int:
        return self.data[self.rear]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()