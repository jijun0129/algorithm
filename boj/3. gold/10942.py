import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
dp = [[0 for _ in range(N)] for _ in range(N)]
M = int(input())

# 같은 수는 무조건 팰린드롬이다.
for i in range(N):
  dp[i][i] = 1
# 연속된 두 수가 같다면 팰린드롬이다.
for i in range(N-1):
  if nums[i] == nums[i+1]:
    dp[i][i+1] = 1
# i+1부터 i+j-1까지 팰린드롬이고, i와 i+j가 같다면 i부터 i+j까지도 팰린드롬이다.
# 이를 이용해 길이가 3 이상인 팰린드롬을 구한다.
for j in range(2, N):
  for i in range(N-j):
    if nums[i] == nums[i+j] and dp[i+1][i+j-1]:
      dp[i][i+j] = 1

for _ in range(M):
  s, e = map(int, input().split())
  print(dp[s-1][e-1])