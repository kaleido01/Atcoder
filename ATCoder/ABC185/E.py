import math
n, m = map(int ,input().split())

al = list(map(int, input().split()))
bl = list(map(int, input().split()))



dp = [[math.inf for _ in range(m+1)] for _ in range(n+1)]


for i in range(n+1):
  for j in range(m+1):
    if i == 0:
      dp[i][j] = j
    elif j == 0:
      dp[i][j] = i
    else:
      # if al[i-1] == bl[j-1]:
      #   dp[i][j] =min(dp[i-1][j] + 1, dp[i][j-1] +1,dp[i-1][j-1])
      # else:
      #   dp[i][j] =min(dp[i-1][j] + 1, dp[i][j-1] +1,dp[i-1][j-1]+1)
      dp[i][j] =min(dp[i-1][j] + 1, dp[i][j-1] +1,dp[i-1][j-1] + (0 if al[i-1] == bl[j-1] else 1))

    
      
# print(dp)
print(dp[n][m])