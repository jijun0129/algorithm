N, k = map(int, input().split())
score = list(map(int, input().split()))
# reverse=True로 내림차순 정렬
score.sort(reverse=True)

print(score[k-1])