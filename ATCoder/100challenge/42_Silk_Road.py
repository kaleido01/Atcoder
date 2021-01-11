n, m = map(int, input().split())

d= [int(input()) for _ in range(n)]
c = [int(input()) for _ in range(m)]


# dp =[[ [float("inf")] * (m-n+1)for _ in range(m+1)] for _ in range(n+1)]
dp =[ [float("inf") for _ in range(m-n+1)]  for _ in range(n+1)]

for i in range (n):
  for j in range (m-n+1):
    dp[i][j] = 0

for i in range(n):
    for j in range(m-n+1):
      if j ==0:
        dp[i+1][0] = dp[i][0] + d[i] * c[i]
      else:
        dp[i+1][j]= min(dp[i][j] + d[i] * c[i+j], dp[i+1][j-1])

print(min(dp[n]))