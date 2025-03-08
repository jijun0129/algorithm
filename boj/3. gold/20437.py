from collections import defaultdict

N = int(input().strip())
for _ in range(N):
  word = input().strip()
  K = int(input().strip())

  # 각 알파벳의 위치를 list로 저장한다. (index를 저장)
  wordDict = defaultdict(list)
  for i in range(len(word)):
    wordDict[word[i]].append(i)

  min = 10000
  max = 0
  for key in wordDict:
    # 알파벳이 K개 이상일 때만 계산
    if len(wordDict[key]) >= K:
      # 알파벳이 K개 있는 경우의 길이를 wordLength에 저장한다.
      for i in range(len(wordDict[key]) - K + 1):
        wordLength = wordDict[key][i + K - 1] - wordDict[key][i] + 1
        # min, max를 갱신
        if wordLength < min:
          min = wordLength
        if max < wordLength:
          max = wordLength

  if min == 10000:
    print(-1)
  else:
    print(min, max)