class Pair:
    def __init__(self, key, val):
        self.key = key
        self.val = val
    
    def __repr__(self):
        return f"({self.key}, {self.val})"

class HashTable:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.hash_map = [None] * self.capacity
    
    def get_hash(self, key):
        return key % self.capacity
    
    def rehash(self):
        self.size = 0
        self.capacity = self.capacity * 2
        
        oldMap = self.hash_map
        self.hash_map = [None] * self.capacity

        for item in filter(None, oldMap):
            self.insert(item.key, item.val)

    def insert(self, key: int, value: int) -> None:
        new_element = Pair(key, value)

        if self.size + 1 >= self.capacity // 2:
            self.rehash()
                
        index = self.get_hash(key)
        print(self.hash_map)
        while True:
            item = self.hash_map[index]

            if item is None or item.key == key:
                self.hash_map[index] = new_element

                if item is None:
                    self.size += 1
                return

            index = (index + 1) % self.capacity                      
        
    def get(self, key: int) -> int:
        index = self.get_hash(key)
        starting_index = index

        while True:
            item = self.hash_map[index]

            if item and item.key == key:
                return item.val
            
            index = (index + 1) % self.capacity

            if index == starting_index:
                return -1

    def remove(self, key: int) -> bool:
        index = self.get_hash(key)
        starting_index = index

        while True:
            item = self.hash_map[index]

            if item and item.key == key:
                self.hash_map[index] = None
                self.size -= 1
                return True
            
            index = (index + 1) % self.capacity

            if index == starting_index:
                return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity
