N = int(input())

# 에라토스테네스의 체를 이용하여 소수를 구한다. 
check = [False, False] + [True] * (N-1)
prime = []
for i in range(2, N+1):
  if check[i]:
    prime.append(i)
    for j in range(2*i, N+1, i):
      check[j] = False

# 두 포인터를 이용하여 sum을 구한다. (연속된 소수의 합)
count = 0
left, right = 0, 1
while left < N and right < N+1:
  num = sum(prime[left:right])
  # N과 같다면 count += 1 후 왼쪽을 이동
  if num == N:
    count += 1
    left += 1
  # N보다 작다면 오른쪽을 이동
  elif num < N:
    right += 1
  # N보다 크다면 왼쪽을 이동
  else:
    left += 1

print(count)