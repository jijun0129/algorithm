from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  N, K = map(int, input().split())
  D = [0] + list(map(int, input().split()))
  
  # 위상정렬을 위해 사용
  dependency = [[] for _ in range(N+1)]
  # inDegree가 0인 건물은 작업 시작
  inDegree = [0 for _ in range(N+1)]
  # 이전까지의 최대 작업시간을 dp에 저장
  dp = [0 for _ in range(N+1)]
  # 그래프 탐색을 위해 queue 사용
  q = deque()

  for i in range(K):
    X, Y = map(int, input().split())
    dependency[X].append(Y)
    inDegree[Y] += 1
  W = int(input())

  for i in range(1, N+1):
    if inDegree[i] == 0:
      q.append(i)

  while q:
    building = q.popleft()
    # dp에 building의 건설시간을 넣는다. 
    dp[building] += D[building]
    for i in dependency[building]:
      # building을 지어야 지을 수 있는 건물들의 건설시간을 업데이트한다. 
      dp[i] = max(dp[i], dp[building])
      inDegree[i] -= 1
      # 먼저 지어져야 하는 건물이 없어지면 queue에 해당 건물을 넣는다. 
      if inDegree[i] == 0:
        q.append(i)
  
  print(dp[W])