import sys
input = sys.stdin.readline

N = int(input())
liquids = list(map(int, input().split()))
liquids.sort()


# 최소를 만드는 값의 위치와 그 값을 저장
min = [0, 0, 0, 3000000000]
# 밖에 for문을 통해 하나의 값을 정하고 안에 while문을 통해 나머지 두 값을 찾음
# 이때, left와 right는 i+1과 N-1로 초기화
for i in range(N-2):
    left, right = i+1, N-1
    while left < right:
        sum = liquids[i] + liquids[left] + liquids[right]
        # 최소값 갱신
        if abs(sum) < min[3]:
            min = [liquids[i], liquids[left], liquids[right], abs(sum)]

        # 음수라면 값이 더 커져야 하므로 left를 오른쪽으로 이동
        if sum < 0:
            left += 1
        # 양수라면 값이 더 작아져야 하므로 right를 왼쪽으로 이동
        elif sum > 0:
            right -= 1
        # 0이라면 더 이상 탐색할 필요가 없으므로 종료
        else:
            print(liquids[i], liquids[left], liquids[right])
            exit(0)

# 저장된 위치로 값을 출력
print(min[0], min[1], min[2])