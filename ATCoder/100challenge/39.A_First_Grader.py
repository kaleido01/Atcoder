n = int(input())

a = list(map(int, input().split()))

dp = [[0] * 25 for _ in range(n)]

# for i in range(n):
dp[1][a[0]] = 1
for i in range(1, n-1):
  for j in range(21):
    # 足し算記号の時
    # if 0 <= (j + a[i]) <=20 and j - a[i]>=0:
    #   if dp[i][j - a[i]] >= 0:
    #     dp[i+1][j] += dp[i][j - a[i]]
    # # 引き算記号の時
    # elif 0 <= j - a[i] <=20 and j + a[i]<=20:
    #   if dp[i][j + a[i]] >= 0:
    #     dp[i+1][j] += dp[i][j + a[i]]
    if j-a[i] >=0:
      dp[i+1][j] += dp[i][j - a[i]]
    if j+a[i] <= 20:
       dp[i+1][j] += dp[i][j + a[i]]

print(dp[n-1][a[-1]])