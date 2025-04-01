import sys
input = sys.stdin.readline
# 재귀 탐색의 깊이를 늘려준다. 
sys.setrecursionlimit(10**6)

T = int(input())
for _ in range(T):
  M, N, K = map(int, input().split())
  count = 0
  board = [[0 for _ in range(M)] for _ in range(N)]
  visited = [[False for _ in range(M)] for _ in range(N)]
  # 가로가 X, 세로가 Y 이기 때문에 board[Y][X]
  for _ in range(K):
    X, Y = map(int, input().split())
    board[Y][X] = 1

  # dfs를 구현
  def dfs(y, x):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= ny < N and 0 <= nx < M and  board[ny][nx] == 1 and not visited[ny][nx]:
        visited[ny][nx] = True
        dfs(ny, nx)

  # board[i][j]가 1이고 visited[i][j]가 False이면 다른 구역의 배추이다. 
  for i in range(N):
    for j in range(M):
      if board[i][j] == 1 and not visited[i][j]:
        visited[i][j] = True
        dfs(i, j)
        count += 1
  print(count)