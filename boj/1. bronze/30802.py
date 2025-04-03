N = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())

# size 각각을 돌면서 묶음 수를 계산
ansT = 0
for i in range(len(size)):
  if size[i] % T != 0:
    setSize = size[i] // T + 1
  else:
    setSize = size[i] // T
  ansT += setSize
print(ansT)

# 나눈 값은 묶음 수, 나머지는 1개씩
divP = N // P
modP = N % P
print(divP, modP)