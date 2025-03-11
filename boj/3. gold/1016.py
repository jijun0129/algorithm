min, max = map(int, input().split())

answer = max - min + 1
number = [False] * (max - min + 1)

for i in range(2, int(max**0.5 + 1)):
  square = i ** 2
  # min에서 max 사이의 제곱수를 제거해나간다. 
  for j in range(((min-1)//square+1)*square, max+1, square):
    if not number[j - min]:
      # 배열이 min부터 저장하기 때문에 j - min
      number[j - min] = True
      answer -= 1
print(answer)
