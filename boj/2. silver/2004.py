n, m = map(int, input().split())

# n!에 대해서 n//2 + n//4 + n//8 + ... 를 구하면 2의 개수를 구할 수 있다.
def countTwo(n):
  two = 0
  while n != 0:
    n = n // 2
    two += n
  
  return two

# n!에 대해서 n//5 + n//25 + n//125 + ... 를 구하면 5의 개수를 구할 수 있다.
def countFive(n):
  five = 0
  while n != 0:
    n = n // 5
    five += n
  
  return five

# 2와 5의 개수 중 작은 값을 구한다.
count2 = countTwo(n) - countTwo(n - m) - countTwo(m)
count5 = countFive(n) - countFive(n - m) - countFive(m)
count = min(count2, count5)

print(count)