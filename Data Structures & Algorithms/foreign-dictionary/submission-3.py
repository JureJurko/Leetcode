from collections import defaultdict

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        if len(words) == 1:
            return words[0]

        def is_prefix(a, b):
            return len(a) < len(b) and b[:len(a)] == a
        
        def get_letter_dependencies(a, b):
            for i, j in zip(a, b):
                if i == j:
                    continue
                elif i != j:
                    adj[i].add(j) # Slovo "i" dolazi nakon slova "j"
                    break
            
            for i in a:
                if i not in adj:
                    adj[i] = set()
            
            for j in b:
                if j not in adj:
                    adj[j] = set()
        
        adj = defaultdict(set)

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if is_prefix(words[j], words[i]):
                    return ""
                
                get_letter_dependencies(words[i], words[j])

        topological_sort = list()
        visited = set()
        current_path = set()
        
        def dfs(curr):
            if curr in current_path:
                return False
            else:
                current_path.add(curr)
            if curr in visited:
                current_path.remove(curr)
                return True
            visited.add(curr)

            letters_that_come_later = adj.get(curr) or []
            for letter in letters_that_come_later:
                ret = dfs(letter)
                if not ret:
                    return False
            topological_sort.append(curr)
            current_path.remove(curr)
            return True

        for i in adj:
            ret = dfs(i)
            if not ret:
                return ""
            
        topological_sort.reverse()
        return "".join(topological_sort)

                

