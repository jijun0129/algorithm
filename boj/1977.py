M = int(input().strip())
N = int(input().strip())

sum = 0
min = 100
# 100부터 1까지 거꾸로 돌면서 제곱수를 찾는다.
# 제곱수가 M과 N 사이에 있으면 sum에 더하고 min에 저장한다.
for i in range(100, 0, -1):
  if i**2 >= M and i**2 <= N:
    sum += i**2
    min = i**2

if sum == 0:
  print(-1)
else:
  print(sum)
  print(min)