import heapq
from typing import List

INF = int(1e9)


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distance = [INF] * (n + 1)
        graph = [[] for i in range(n + 1)]
        for ls in times:
            graph[ls[0]].append((ls[1], ls[2]))

        def dijkstra(start):
            q = []
            heapq.heappush(q, (0, start))
            distance[start] = 0
            while q:
                dist, cur = heapq.heappop(q)
                if distance[cur] < dist:
                    continue
                for i in graph[cur]:
                    cost = dist + i[1]
                    if cost < distance[i[0]]:
                        distance[i[0]] = cost
                        heapq.heappush(q, (cost, i[0]))

        dijkstra(k)
        max = 0
        for i in range(1,len(distance)):
            if distance[i] == INF:
                return -1
            if distance[i] > max:
                max = distance[i]
                
        return max
