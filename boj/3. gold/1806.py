import sys
input = sys.stdin.readline

N, S = map(int, input().split())
num = [0] + list(map(int, input().split()))
# prefix sum을 구한다. 
# 맨 앞에 0을 추가하여 모든 첫번째 값부터 마지막 판까지 더한 것도 계산
psum = num
for i in range(1, N+1):
  psum[i] += psum[i-1]

count = N+1
# 두 포인터를 처음부터 시작해서 S보다 크면 left를 이동
# S보다 작으면 right를 이동시킨다. 
left, right = 0, 1
while left <= N:
  if psum[right] - psum[left] < S:
    if right < N:
      right += 1
    else:
      break
  else:
    # 길이가 더 짧으면 업데이트
    if right - left < count:
      count = right - left
    left += 1

# count가 업데이트하지 않으면 0을 출력
if count == N+1:
  print(0)
else:
  print(count)