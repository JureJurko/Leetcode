class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        for idx, (u, v, w) in enumerate(edges):
            adj[u].append((v, w, idx))
            adj[v].append((u, w, idx))

        def run_prim(skip_idx: int = -1, force_idx: int = -1) -> int:
            visited = set()
            min_heap = []
            total_weight = 0

            if force_idx != -1:
                u, v, w = edges[force_idx]
                visited.add(u)
                visited.add(v)
                total_weight = w
                
                for neighbor, weight, idx in adj[u]:
                    if idx != force_idx:
                        heapq.heappush(min_heap, (weight, neighbor))
                for neighbor, weight, idx in adj[v]:
                    if idx != force_idx:
                        heapq.heappush(min_heap, (weight, neighbor))
            else:
                visited.add(0)
                for neighbor, weight, idx in adj[0]:
                    if idx != skip_idx:
                        heapq.heappush(min_heap, (weight, neighbor))

            while min_heap and len(visited) < n:
                weight, node = heapq.heappop(min_heap)
                if node in visited:
                    continue
                
                visited.add(node)
                total_weight += weight

                for neighbor, n_weight, idx in adj[node]:
                    if idx != skip_idx and neighbor not in visited:
                        heapq.heappush(min_heap, (n_weight, neighbor))

            return total_weight if len(visited) == n else float('inf')

        std_weight = run_prim()

        critical = []
        pseudo_critical = []

        for i in range(len(edges)):
            if run_prim(skip_idx=i) > std_weight:
                critical.append(i)
            elif run_prim(force_idx=i) == std_weight:
                pseudo_critical.append(i)

        return [critical, pseudo_critical]