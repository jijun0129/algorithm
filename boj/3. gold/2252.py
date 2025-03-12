from collections import deque
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
queue = deque()

answer = []
dependency = [[] for _ in range(N+1)]
inDegree = [0 for _ in range(N+1)]

for i in range(M):
  a, b = map(int, input().split())
  # 입력을 기준으로 위상 정렬한다. 
  dependency[a].append(b)
  # in-degree를 늘려준다. 
  inDegree[b] += 1

for i in range(1, N+1):
  # in-degree가 0이라면 키가 더 작은 친구와 비교한 적이 없다. 
  if inDegree[i] == 0:
    queue.append(i)

while queue:
  person = queue.popleft()
  print(person, end=' ')
  for i in dependency[person]:
    # in-degree를 1씩 줄여가면서 더 작은 친구와 비교한 적이 없게 되면 queue에 추가한다. 
    inDegree[i] -= 1
    if inDegree[i] == 0:
      queue.append(i)



# DFS 방식으로 구현했더니 RecursionError 발생
"""
from collections import defaultdict
import sys

def dfs(person):
  visited[person] = True
  while len(dependency[person]) > 0:
    nextPerson = dependency[person].pop()
    if not visited[nextPerson]:
      dfs(nextPerson)
  print(person, end=' ')

input = sys.stdin.readline
N, M = map(int, input().split())

dependency = defaultdict(list)
visited = defaultdict(lambda: False)

for i in range(M):
  a, b = map(int, input().split())
  dependency[b].append(a)

for i in range(1, N+1):
  if not visited[i]:
    dfs(i)"

"""