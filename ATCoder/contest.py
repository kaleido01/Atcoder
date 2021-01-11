n = int(input())

p = list(map(int, input().split()))

dp = [ [0 for _ in range(10010)] for _ in range(n+1)]
dp[0][0]=1

for i in range(n):
  for j in range(10010):
    if j >= p[i]:
      if dp[i][j-p[i]]+dp[i][j]>= 1:
        dp[i+1][j] = 1
    else:
      dp[i+1][j] = dp[i][j]
print(sum(dp[n]))
