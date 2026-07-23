import heapq
from collections import defaultdict


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float],
                       start_node: int, end_node: int) -> float:
        adj = defaultdict(list)
        for (a, b), p in zip(edges, succProb):
            adj[a].append((b, p))
            adj[b].append((a, p))

        best = {start_node: 1.0}
        done = set()
        heap = [(-1.0, start_node)]
        while heap:
            neg_p, node = heapq.heappop(heap)
            if node in done:
                continue
            p = -neg_p
            if node == end_node:
                return p
            done.add(node)

            for nxt, w in adj[node]:
                if nxt in done:
                    continue
                cand = p * w
                if cand > best.get(nxt, 0.0):
                    best[nxt] = cand
                    heapq.heappush(heap, (-cand, nxt))
        return 0.0