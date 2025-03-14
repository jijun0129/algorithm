import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  N = int(input())
  ranking = []
  for _ in range(N):
    ranking.append(list(map(int, input().split())))

  # 기본 아이디어: 1차 서류를 등수로 정렬한 후 2차 면접을 판단
  # 아래로 내려가면 서류 등수는 무조건 낮기 때문에 면접 등수가 낮은지 확인하면 된다. 
  ranking.sort(key=lambda x: x[0])
  maxRank = ranking[0][1]
  failed = 0
  for i in range(1, N):
    # 가장 높은 등수보다 등수가 낮다면 탈락
    if ranking[i][1] > maxRank:
      failed += 1
    # 더 높은 등수라면 maxRank를 업데이트한다. 
    else:
      maxRank = ranking[i][1]
  print(N - failed)