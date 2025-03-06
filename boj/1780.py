import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
answer = [0, 0, 0]

def check(x, y, n):
  # 사이즈가 1이면 해당 숫자의 개수를 1 증가시킨다.
  if n == 1:
    answer[paper[x][y]+1] += 1
    return

  # 1, 0, -1의 개수를 세어서 n*n이면 해당 숫자의 개수를 1 증가시킨다.
  countOne, countZero, countMinusOne = 0, 0, 0
  for i in range(x, x+n):
    for j in range(y, y+n):
      if paper[i][j] == 1:
        countOne += 1
      elif paper[i][j] == 0:
        countZero += 1
      else:
        countMinusOne += 1

  if countOne == n*n:
    answer[2] += 1
  elif countZero == n*n:
    answer[1] += 1
  elif countMinusOne == n*n:
    answer[0] += 1
  # 개수가 다르다면 9등분하여 재귀적으로 확인한다.
  else:
    check(x, y, n//3)
    check(x, y+n//3, n//3)
    check(x, y+2*n//3, n//3)

    check(x+n//3, y, n//3)
    check(x+n//3, y+n//3, n//3)
    check(x+n//3, y+2*n//3, n//3)

    check(x+2*n//3, y, n//3)
    check(x+2*n//3, y+n//3, n//3)
    check(x+2*n//3, y+2*n//3, n//3)

check(0, 0, N)
for i in answer:
  print(i)