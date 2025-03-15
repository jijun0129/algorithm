import sys
input = sys.stdin.readline

def distance(x, y, a, b):
  return (x-a)**2 + (y-b)**2

T = int(input())
for _ in range(T):
  count = 0
  x1, y1, x2, y2 = map(int, input().split())
  N = int(input())
  for _ in range(N):
    cx, cy, cr = list(map(int, input().split()))

    dist1 = distance(x1, y1, cx, cy)
    dist2 = distance(x2, y2, cx, cy)

    # 원 안에 있다가 밖으로 나가는경우 or 원 밖에 있다가 안으로 들어오는 경우
    # 이 경우에만 원의 경계를 지나는 것이 최소가 된다. 
    if (dist1 < cr**2 and dist2 > cr**2) or (dist1 > cr**2 and dist2 < cr**2):
      count += 1
  
  print(count)