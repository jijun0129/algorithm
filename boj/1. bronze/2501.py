N, K = map(int, input().strip().split())

# N의 약수 중 K번째로 작은 수를 찾는다.
# N // 2보다 큰 약수는 N 하나밖에 없다. 
for i in range(1, N // 2 + 1):
  if N % i == 0:
    K -= 1
  if K == 0:
    print(i)
    break

# 1보다 크면 K보다 약수가 적다. 1이면 N이 약수이다.
if K > 1:
  print(0)
elif K == 1:
  print(N)