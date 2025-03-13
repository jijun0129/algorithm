N = int(input())
callList = list(map(int, input().split()))

M, Y = 0, 0
for call in callList:
  # 요금이 증가하는 시간으로 나눈 후 나머지 시간을 계산하기 위해 +1
  Y += 10 * (call // 30 + 1)
  M += 15 * (call // 60 + 1)
  
if Y == M:
  print("Y M %d" %Y)
elif Y > M:
  print("M %d" %M)
else:
  print("Y %d" %Y)