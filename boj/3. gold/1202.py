import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())
jewel = [list(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for i in range(K)]
answer = 0

# 무게 순으로 정렬
jewel.sort(key=lambda x: -x[0])
bags.sort(reverse=True)

hq = []

while bags:
  # 가장 가벼운 가방을 꺼낸다. 
  bag = bags.pop()
  while jewel:
    # 가장 가벼운 보석을 꺼낸다. 
    weight, value = jewel.pop()
    if bag >= weight:
      # 가방에 넣을 수 있다면 최대 힙에 추가
      heapq.heappush(hq, -value)
    else:
      # 넣을 수 없다면 다시 보석 리스트에 추가
      jewel.append([weight, value])
      break
  # 힙에 있는 가장 가치가 큰 보석을 꺼내서 가방에 넣는다. 
  # 이전에 힙에 더 큰 가치의 보석이 들어간다면 그 보석이 가방에 들어간다. 
  if hq:
    answer -= heapq.heappop(hq)

print(answer)