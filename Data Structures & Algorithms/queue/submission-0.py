class Node:
    def __init__(self, value=0, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class Deque:
    def __init__(self):
        self.head = self.tail = None

    def isEmpty(self) -> bool:
        if self.head is None:
            return True
        return False

    def append(self, value: int) -> None:
        new_node = Node(value=value)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            prev = self.tail
            prev.next = new_node
            new_node.prev = prev
            self.tail = new_node

    def appendleft(self, value: int) -> None:
        new_node = Node(value=value)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_next = self.head
            new_node.next = new_next
            new_next.prev = new_node
            self.head = new_node

    def pop(self) -> int:
        if self.tail is None:
            return -1
        else:
            ret_value = self.tail.value
            if self.tail == self.head:
                self.head = self.tail = None
                return ret_value
            else:
                self.tail.prev.next = None
                self.tail = self.tail.prev
                return ret_value


    def popleft(self) -> int:
        if self.head is None:
            return -1
        else:
            ret_value = self.head.value
            if self.head == self.tail:
                self.head = self.tail = None
                return ret_value
            else:
                self.head.next.prev = None
                self.head = self.head.next
                return ret_value
        
