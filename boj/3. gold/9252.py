word1 = list(input().rstrip())
word2 = list(input().rstrip())

dp = [['' for _ in range(len(word1) + 1)] for _ in range(len(word2) + 1)]
for i in range(1, len(word2) + 1):
  for j in range(1, len(word1) + 1):
    # 문자가 같다면 dp[i][j]는 dp[i-1][j-1]까지 계산한 것에 문자를 더한 것이다.
    if word2[i - 1] == word1[j - 1]:
      dp[i][j] = dp[i - 1][j - 1] + word2[i - 1]
    # 다르다면 dp[i][j]는 dp[i-1][j]와 dp[i][j-1] 중 길이가 더 긴 것을 선택한다.
    else:
      if len(dp[i - 1][j]) > len(dp[i][j - 1]):
        dp[i][j] = dp[i - 1][j]
      else:
        dp[i][j] = dp[i][j - 1]

print(len(dp[-1][-1]))
print(dp[-1][-1])