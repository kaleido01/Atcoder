d, n = map(int, input().split())

t = [int(input()) for _ in range(d)]

a = [0] *(n)
b = [0] *(n)
c = [0] *(n)

for i in range(n):
  a[i], b[i], c[i] = map(int, input().split())
  
  
dp =[[0 for _ in range(n)] for _ in range(d+1)]

for i in range(d):
  for j in range(n):
    for k in range(n):
      if i == 0:
        if a[j] <= t[i]<= b[j]:
          dp[1][j] = 0
      elif a[k] <= t[i-1]<= b[k] and a[j] <= t[i] <= b[j]:
        dp[i+1][j] = max(dp[i+1][j], dp[i][k] + abs(c[k] - c[j]))

print(max(dp[d]))