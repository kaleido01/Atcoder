n,m = map(int, input().split())

coin = list(map(int, input().split()))


dp=[[500010 for _ in range (50010)] for _ in range(25)]

for i in range (m):
  dp[i][0] = 0

for i in range (m):
  for j in range (n+1):
    if j >= coin[i]:
      dp[i+1][j] = min(dp[i+1][j-coin[i]] + 1, dp[i][j])
    else:
      dp[i+1][j] = dp[i][j]

# for i in range (m):
#   for j in range (n+1):
#     if j >= coin[i]:
#       dp[i+1][j] = min(dp[i][j-coin[i]] + 1, dp[i][j])
#     else:
#       dp[i+1][j] = dp[i][j]

# print(dp)
print(dp[m][n])