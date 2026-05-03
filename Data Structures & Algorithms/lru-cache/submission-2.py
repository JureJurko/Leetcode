class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

    def __repr__(self):
        return str(self.val)

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        self.left = self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def insert(self, node):
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.prev = prev
        node.next = next 

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.remove(node)
        self.insert(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        new_node = Node(key, value)
        if key in self.cache:
            node_to_remove = self.cache[key]
            self.remove(node_to_remove)
            self.insert(new_node)
            self.cache[key] = new_node
            return
        if len(self.cache) == self.capacity:
            node_to_remove = self.left.next
            self.remove(node_to_remove)
            del self.cache[node_to_remove.key]
                

        self.insert(new_node)
        self.cache[key] = new_node
        















        
