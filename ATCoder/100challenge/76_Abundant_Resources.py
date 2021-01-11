n = int(input())

a = list(map(int, input().split()))



dp = [ sum(a[0:i+1]) for i in range(n) ]

dp.insert(0,0)
ans = 0
for i in range(1,n+1):
  for j in range(1,n+2-i):
    ans =max(ans,dp[i+j-1] - dp[j-1])
  print(ans)
  ans=0