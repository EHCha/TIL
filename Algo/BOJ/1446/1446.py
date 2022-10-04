import heapq
import sys
sys.stdin = open('1446.txt')


def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0
    while q:
        d, now = heapq.heappop(q)
        if distance[now] < d:
            continue
        for j in graph[now]:
            cost = d + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))


INF = 10000
V, E = map(int, input().split())
graph = [[] for _ in range(E+1)]
distance = [INF]*(E+1)

for i in range(E):
    graph[i].append((i+1, 1))

for _ in range(V):
    u, v, w = map(int, input().split())
    if v > E:
        continue
    graph[u].append((v, w))

dijkstra(0)
print(distance[E])
