import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

V = int(input())

tree = [[] for _ in range(V+1)]
visited = [-1] * (V+1)
for _ in range(V):
  data = list(map(int, input().split()))
  for i in range(1, len(data)-2, 2):
    tree[data[0]].append((data[i], data[i+1]))

# dfs를 돌면서 visitied에 각 노드까지의 거리를 저장
def dfs(node, weight):
  for child, w in tree[node]:
    if visited[child] == -1:
      nowWeight = weight + w
      visited[child] = nowWeight
      dfs(child, nowWeight)

# dfs를 2번 돌리는 방식을 사용
# 첫 번째 dfs는 1번 노드에서 시작하여 가장 먼 노드를 찾는다.
visited[1] = 0
dfs(i, 0)

index, maxWeight = 0, 0
for i in range(1, len(visited)):
  if maxWeight < visited[i]:
    maxWeight = visited[i]
    index = i

# 두 번째 dfs는 첫 번째 dfs에서 찾은 노드에서 시작하여 가장 먼 노드를 찾는다.
# 이때의 거리가 트리의 지름이다.
visited = [-1] * (V+1)
visited[index] = 0
dfs(index, 0)
print(max(visited))