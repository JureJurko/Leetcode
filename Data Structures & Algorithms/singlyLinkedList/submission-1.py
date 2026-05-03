class LinkedList:
    
    def __init__(self):
        self.linked_list = []
    
    def get(self, index: int) -> int:
        if len(self.linked_list) <= index:
            return -1
        
        return self.linked_list[index]
        
    def insertHead(self, val: int) -> None:
        self.linked_list.insert(0, val)
        

    def insertTail(self, val: int) -> None:
        self.linked_list.append(val)
        

    def remove(self, index: int) -> bool:
        if len(self.linked_list) <= index:
            return False
        
        del self.linked_list[index]
        return True

    def getValues(self) -> List[int]:
        return self.linked_list
        
