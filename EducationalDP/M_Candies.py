n,p = map(int, input().split())
a = list(map(int, input().split()))


dp =[ [0 for _ in range(p+1)] for _ in range(n+1)]

mod = 10**9 +7
for i in range(n):
  dp[i][0] = 1
  
x = [0] * (p+2)
x[0] = 0
for i in range(n):
  for j in range(1, p+2):
    x[j] = dp[i][j-1]+ x[j-1] % mod
    # for k in range(a[i]+1):
    # if j-a[i] >=0:
    #   dp[i+1][j] = x[j] - x[j-a[i]]
    # else:
    #   dp[i+1][j] = x[j]
  # print(x)
  for j in range(p+1):
    dp[i+1][j] = (x[j+1] - x[max(0, j-a[i])] )% mod

# print(dp)
print(dp[n][p])