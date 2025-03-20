import sys
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
max_num = 2**31
# dp[i][j]: i부터 j까지 행렬을 곱했을 때의 최소 연산 횟수
dp = [[max_num for _ in range(N)] for _ in range(N)]
for i in range(N):
  dp[i][i] = 0
for i in range(1, N):
  for j in range(N-i):
    # j부터 k까지 연산 이후 k+1 부터 j+i까지 연산을 한 것의 최소를 구한다. 
    for k in range(j, j+i):
      dp[j][j+i] = min(dp[j][j+i], dp[j][k] + dp[k+1][j+i] + matrix[j][0] * matrix[k][1] * matrix[j+i][1])

print(dp[0][-1])