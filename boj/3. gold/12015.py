import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
number = list(map(int, input().split()))
lis = [number[0]]

# lis의 값을 업데이트하면서 길이를 출력
# lis가 실제 lis는 아니지만 길이가 lis의 길이와 같다. 
for num in number:
  # lis의 제일 큰 값보다 크다. 
  if lis[-1] < num:
    lis.append(num)
  # 아닌 경우는 num의 lis의 위치를 찾아서 값을 대입한다. 
  else:
    index = bisect_left(lis, num)
    lis[index] = num

print(len(lis))