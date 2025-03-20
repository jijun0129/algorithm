import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

T = int(input())
for _ in range(T):
  N = int(input())
  students = [0] + list(map(int, input().split()))
  visited = [False] * (N + 1)
  count = 0

  def dfs(i):
    global count
    visited[i] = True
    team.append(i)
    selected = students[i]
    # 사이클이 만들어졌다면
    if visited[selected]:
      # 사이클이 형성된 시점부터 길이를 계산
      if selected in team:
        count += len(team[team.index(selected):])
    # 사이클이 아니라면 계속해서 탐색
    else:
      dfs(selected)
      

  for i in range(1, N + 1):
    if not visited[i]:
      team = []
      dfs(i)
  print(N - count)