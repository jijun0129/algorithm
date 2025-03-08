N, M = map(int, input().split())
# 1번 바구니부터 N번 바구니까지 사용(0번 바구니는 사용 X)
bag = [0] * (N + 1)

for _ in range(M):
    i, j, k = map(int, input().split())
    # i번 바구니부터 j번 바구니까지 k로 값 설정정
    for a in range(i, j+1):
        bag[a] = k

# 1번 바구니부터 N번 바구니까지 출력
for i in range(1, len(bag)):
    print(bag[i], end=' ')