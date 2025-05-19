# 구간 합을 구하는데 값의 변경이 많이 일어나는 경우 -> 세그먼트 트리를 생각
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

data = []
for i in range(N):
  data.append(int(input().rstrip()))

tree = [0 for _ in range(4*len(data))]
# 세그먼트 트리 초기화
# 세그먼트 트리의 크기는 4배로 잡는다(중간 노드 필요)
def init(start, end, index):
  if start == end:
    # 리프 노드라면 data의 값을 넣는다. 
    tree[index] = data[start]
    return tree[index]
  mid = (start + end) // 2
  # 중간 노드라면 각각 자식 노드의 합을 넣는다. 
  tree[index] = init(start, mid, index*2) + init(mid+1, end, index*2+1)
  return tree[index]

def update(start, end, index, what, value):
  # 범위 밖이라면 그냥 리턴한다.(기존 값 유지)
  if start > what or end < what:
    return tree[index]
  if start == end:
    tree[index] = value
    return tree[index]
  mid = (start + end) // 2
  tree[index] = update(start, mid, index*2, what, value) + update(mid+1, end, index*2+1, what, value)
  return tree[index]

def sum(start, end, index, what1, what2):
  # 범위 밖이라면 0을 리턴한다. (더하면 안되기 때문)
  if start > what2 or end < what1:
    return 0
  if start >= what1 and end <= what2:
    return tree[index]
  mid = (start + end) // 2
  return sum(start, mid, index*2, what1, what2) + sum(mid+1, end, index*2+1, what1, what2)

# 세그먼트 트리의 index는 1부터 시작(재귀로 쉽게 구현하기 위해)
init(0, len(data) - 1, 1)

for i in range(M + K):
  a, b, c = map(int, input().split())
  if a == 1:
    # a = 1이면 b(index는 b-1)번째 수를 c로 바꾼다
    update(0, len(data) - 1, 1, b - 1, c)
  else:
    # a = 2이면 b(index는 b-1)부터 c(index는 c-1)까지의 합을 구한다
    print(sum(0, len(data) - 1, 1, b - 1, c - 1))