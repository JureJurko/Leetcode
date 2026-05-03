class DynamicArray:
    
    def __init__(self, capacity: int):
        self.darray = [0] * capacity
        self.capacity = capacity
        self.length = 0

    def get(self, i: int) -> int:
        return self.darray[i]

    def set(self, i: int, n: int) -> None:
        self.darray[i] = n

    def pushback(self, n: int) -> None:
        if self.capacity <= self.length:
            self.resize()
        
        self.darray[self.length] = n
        self.length += 1 

    def popback(self) -> int:
        self.length -= 1
        return self.darray[self.length]

    def resize(self) -> None:
        self.capacity *= 2
        new_array = [0] * self.capacity

        for i in range(self.length):
            new_array[i] = self.darray[i]
        
        self.darray = new_array

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity