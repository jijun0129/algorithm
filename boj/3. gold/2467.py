import sys
input = sys.stdin.readline

N = int(input())
liquids = list(map(int, input().split()))

left, right = 0, N-1
# 최소를 만드는 값의 위치와 그 값을 저장
min = [0, 0, 2000000000]
while left < right:
    sum = liquids[left] + liquids[right]
    # 최소값 갱신
    if abs(sum) < min[2]:
        min = [liquids[left], liquids[right], abs(sum)]
    # 음수라면 값이 더 커져야 하므로 left를 오른쪽으로 이동
    if sum < 0:
        left += 1
    # 양수라면 값이 더 작아져야 하므로 right를 왼쪽으로 이동
    else:
        right -= 1

# 저장된 위치로 값을 출력
print(min[0], min[1])