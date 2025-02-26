N, M = map(int, input().split())
bag = [i for i in range(1, N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    # i가 들어있는 바구니 부터 역순으로 바꾼다. 
    bag[i-1:j] = bag[i-1:j][::-1]
print(*bag)
