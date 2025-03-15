import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
number = list(map(int, input().split()))
lis = [number[0]]
dp = [(0, number[0])]

# 기존에 LIS를 구하는 방법으로 lis배열 생성
# dp에 lis에 추가한 index와 값을 추가
for num in number:
  if lis[-1] < num:
    lis.append(num)
    dp.append((len(lis) - 1, num))
  else:
    index = bisect_left(lis, num)
    lis[index] = num
    dp.append((index, num))

print(len(lis))

# dp의 index가 length와 같은 경우의 값이 lis의 값
# 역순으로 answer에 들어가므로 역순으로 출력해주면 된다. 
maxLength = len(lis) - 1
answer = []
for i in range(len(dp) - 1, -1, -1):
  if dp[i][0] == maxLength:
    answer.append(dp[i][1])
    maxLength -= 1

print(*answer[::-1])