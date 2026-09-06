from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_dict = defaultdict(list)

        for i in range(len(prerequisites)):
            course, required_course = prerequisites[i]
            adj_dict[course].append(required_course)
        
        visited = set()
        topological_sort = []
        current_path = set()

        def dfs(curr):
            is_valid = True
            if curr in current_path:
                return False
            else:
                current_path.add(curr)
            if curr in visited:
                current_path.remove(curr)
                return True


            visited.add(curr)

            required_courses = adj_dict.get(curr) or []
            for course in required_courses:
                is_valid = dfs(course)

                if not is_valid:
                    return is_valid 

            topological_sort.append(curr)
            current_path.remove(curr)

            return is_valid
            

        for i in range(numCourses):
            is_valid = dfs(i)
            if not is_valid:
                return []
        return topological_sort
