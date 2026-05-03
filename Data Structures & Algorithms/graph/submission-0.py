from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.graph:
            self.graph[src] = []
        if dst not in self.graph:
            self.graph[dst] = []
        self.graph[src].append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src in self.graph and dst in self.graph and dst in self.graph[src]:
            self.graph[src].remove(dst)
            return True
        
        return False

    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()
        queue = deque()
        
        queue.append(src)
        visited.add(src)

        while queue:
            for i in range(len(queue)):
                curr_node = queue.popleft()
                if curr_node == dst:
                    return True
                
                for node in self.graph[curr_node]:
                    if node not in visited:
                        queue.append(node)
                        visited.add(node)
        
        return False
