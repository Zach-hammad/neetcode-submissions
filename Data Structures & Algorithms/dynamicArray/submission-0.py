class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [0]*capacity
        self.capacity = capacity
        self.length = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.capacity == self.length:
            self.resize()
        self.arr[self.length] = n
        self.length+=1

    def popback(self) -> int:
        self.length -=1
        return self.arr[self.length]

    def resize(self) -> None:
        new_arr = [0] * (2 * self.capacity)
        for i in range(self.length):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.capacity *=2

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity