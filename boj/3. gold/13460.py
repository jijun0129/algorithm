from collections import deque

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
for i in range(1, N-1):
  for j in range(1, M-1):
    # R, B의 위치를 기록
    if board[i][j] == 'R':
      ry, rx = i, j
    if board[i][j] == 'B':
      by, bx = i, j

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(ry, rx, by, bx):
  q = deque()
  q.append((ry, rx, by, bx))
  visited = []
  count = 0
  while q:
    # deque에 있는 것을 모두 비우고 나면 count+1을 수행
    for _ in range(len(q)):
      ry, rx, by, bx = q.popleft()
      # 10회 이상 수행하면 불가능
      if count > 10:
        print(-1)
        return
      # O에 도달하면 횟수를 출력
      if board[ry][rx] == 'O':
        print(count)
        return
      
      for i in range(4):
        # 이동할 수 있는 만큼 r을 이동
        nry, nrx = ry, rx
        while True:
          nry += dy[i]
          nrx += dx[i]
          if board[nry][nrx] == '#':
            nry -= dy[i]
            nrx -= dx[i]
            break
          if board[nry][nrx] == 'O':
            break
        # 이동할 수 있는 만큼 b를 이동
        nby, nbx = by, bx
        while True:
          nby += dy[i]
          nbx += dx[i]
          if board[nby][nbx] == '#':
            nby -= dy[i]
            nbx -= dx[i]
            break
          if board[nby][nbx] == 'O':
            break
        # 파란 구슬이 들어가면 계산 x
        if board[nby][nbx] == 'O':
          continue
        
        # 같은 장소에 있을 수 없기 때문에 먼 거리를 이동한 구슬이 한칸 이전 위치에 있음
        if nry == nby and nrx == nbx:
          if abs(nry - ry) + abs(nrx - rx) > abs(nby - by) + abs(nbx - bx):
            nry -= dy[i]
            nrx -= dx[i]
          else:
            nby -= dy[i]
            nbx -= dx[i]

        # 방문하지 않았다면 deque에 추가
        if (nry, nrx, nby, nbx) not in visited:
          q.append((nry, nrx, nby, nbx))
          visited.append((nry, nrx, nby, nbx))
    count += 1
  print(-1)

bfs(ry, rx, by, bx)
