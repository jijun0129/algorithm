import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

# 시작하는 위치를 찾고 1인 값들을 -1로 바꿔준다. 
si, sj = 0, 0
for i in range(N):
  for j in range(M):
    if board[i][j] == 1:
      board[i][j] = -1
    if board[i][j] == 2:
      si, sj = i, j

# bfs를 이용하여 거리를 업데이트한다. 
q = deque()
dist = 0
visited[si][sj] = True
q.append((si, sj))
while q:
  # 이전에 queue에 들어간 위치는 dist가 같다.
  size = len(q)
  for i in range(size):
    y, x = q.popleft()
    board[y][x] = dist
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]
      if 0 <= ny < N and 0 <= nx < M and board[ny][nx] == -1 and not visited[ny][nx]:
        visited[ny][nx] = True
        q.append((ny, nx))
  dist += 1

# -1이라면 도달하지 못한 곳이기 때문에 -1을 출력한다. 
for i in range(N):
  for j in range(M):
    print(board[i][j], end=' ')
  print()