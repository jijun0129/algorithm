import sys
input = sys.stdin.readline
N, M = map(int, input().split())

people = []
for _ in range(N):
    ride, leave = map(int, input().split())
    # 목적지가 출발지보다 작으면 역방향
    # 순방향 승객은 처음부터 끝까지 이동하면서 알아서 타고 내림
    if ride > leave:
        people.append((leave, ride))
# 내리는 곳 순으로 정렬
people.sort()

merge = 0
if people:
  oldStart, oldEnd = people[0]
  for i in range(1, len(people)):
      newStart, newEnd = people[i]
      # 구간이 겹치는 경우
      if oldEnd >= newStart:
          oldEnd = max(oldEnd, newEnd)
      # 겹치지 않는 경우
      else:
          # 겹치는 경우의 값을 merge에 더해준다.
          merge += oldEnd - oldStart
          oldStart, oldEnd = people[i]
  # 마지막 구간 길이 추가
  merge += oldEnd - oldStart 

answer = M + merge * 2
print(answer)