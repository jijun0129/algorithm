import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  count = 0
  a, b, n = map(int, input().split())
  while a <= n and b <= n:
    if a >= b:
      b += a
    else:
      a += b
    count += 1
  print(count)
  
