from collections import defaultdict

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for prereq, crs in prerequisites:
            adj[crs].append(prereq)
        
        def dfs(crs):
            if crs not in prereqMap:
                prereqMap[crs] = set()
                for prereq in adj[crs]:
                    prereqMap[crs] |= dfs(prereq)
                prereqMap[crs].add(crs)
            return prereqMap[crs]

        prereqMap = {}
        for crs in range(numCourses):
            dfs(crs)
        
        result = []
        for u, v in queries:
            result.append(u in prereqMap[v])
        
        return result