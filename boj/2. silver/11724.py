import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
count = 0

for _ in range(M):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

# dfs를 구현
def dfs(node):
  for child in graph[node]:
    if not visited[child]:
      visited[child] = True
      dfs(child)

# dfs를 실행할 때마다 카운트를 증가시킨다. 
for i in range(1, N+1):
  if not visited[i]:
    dfs(i)
    count += 1

print(count)