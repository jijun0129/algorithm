import sys
from heapq import heappush, heappop

input = sys.stdin.readline

V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]

# MST를 prim 알고리즘으로 구현
def prim(start, weight):
  heapq = [[weight, start]]
  connected = [False] * (V+1)
  sum = 0

  # heapq에서 edge를 하나씩 가져와서 sum을 구한다. 
  while heapq:
    weight, v = heappop(heapq)
    if not connected[v]:
      connected[v] = True
      sum += weight
      for u, w in graph[v]:
        heappush(heapq, [w, u])
  return sum

for _ in range(E):
  a, b, c = map(int, input().split())
  graph[a].append([b, c])
  graph[b].append([a, c])

print(prim(1, 0))