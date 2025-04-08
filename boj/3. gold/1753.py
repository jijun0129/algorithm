import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
heap = []
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

# dijkstra를 이용하여 최단거리를 계산
dist = [INF] * (V + 1)
def dijkstra(start):
    dist[start] = 0
    # heapq를 이용, heap은 첫번째 요소를 기준으로 정렬되므로 weight를 앞에 두어야 한다. 
    heapq.heappush(heap, (0, start))

    while heap:
        weight, node = heapq.heappop(heap)
        # 방문한 노드의 거리가 더 짧은 거리를 계산했다면 continue
        if dist[node] < weight:
            continue

        for w, neighbor in graph[node]:
            if dist[neighbor] > weight + w:
                dist[neighbor] = weight + w
                heapq.heappush(heap, (dist[neighbor], neighbor))

dijkstra(K)
for i in range(1, V+1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])

# 처음에 BFS로 풀었으나, 시간초과가 발생하여 Dijkstra로 변경하였다.
# heapq는 첫번째 요소를 기준으로 정렬되는 점 유의