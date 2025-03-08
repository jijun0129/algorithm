from itertools import combinations, product
from bisect import bisect_left

def solution(dice):
  dic = {}
  # N//2개의 주사위를 combinations로 선택
  for A in combinations(range(len(dice)), len(dice) // 2):
    # B는 A에 속하지 않는 주사위
    B = [i for i in range(len(dice)) if i not in A]

    ASum, BSum = [], []

    # 중복순열으로 주사위의 값을 정한다. 
    for orderProduct in product(range(6), repeat = len(dice) // 2):
      # i는 주사위, j는 주사위의 값
      ASum.append(sum(dice[i][j] for i, j in zip(A, orderProduct)))
      BSum.append(sum(dice[i][j] for i, j in zip(B, orderProduct)))
    BSum.sort()
    # A의 합이 B의 합보다 큰 경우를 센다. (들어갈 위치를 통해 개수를 알 수 있다. )
    wins = sum(bisect_left(BSum, num) for num in ASum)

    # 이긴 횟수를 key로 하여 A의 주사위를 저장
    dic[wins] = list(A)

  # 가장 많이 이긴 횟수를 찾아서 반환
  maxKey = max(dic.keys())
  return [x+1 for x in dic[maxKey]]