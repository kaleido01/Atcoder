import sys

sys.setrecursionlimit(10 ** 8)

h, w = map(int, input().split())
grid = [list(input()) for _ in range(h)]

dp = [[0 for _ in range(w)] for _ in range(h)]
x = [[0 for _ in range(w)] for _ in range(h)]
y = [[0 for _ in range(w)] for _ in range(h)]
z = [[0 for _ in range(w)] for _ in range(h)]
dp[0][0] = 1
# x[0][0] = 1
# y[0][0] = 1
# z[0][0] = 1

# for i in range(h):
#   x[i][0] =1
# for i in range(w):
#   y[0][i] =1

mod = 10**9 +7

# def dfs(h,w):
#   if dp[h][w]>=0:
#     return dp[h][w]
  
#   dp[h][w] = 0
  # for i in range(h):
  #   if grid[h-i-1][w] == "#":
  #     break
    
  #   dp[h][w] += dfs(h-i-1,w) %mod
  # for i in range(w):
  #   if grid[h][w-i-1] == "#":
  #     break
  #   dp[h][w] += dfs(h,w-i-1)%mod
  # for i in range(min(h,w)):
  #   if grid[h-i-1][w-i-1] == "#":
  #     break
  #   dp[h][w] += dfs(h-i-1,w-i-1)%mod

  # return dp[h][w] % mod

# print(dfs(h-1,w-1))


for i in range(h):
  for j in range(w):
    if grid[i][j] == "#":
      continue
    if i-1 >=0:
      x[i][j] = (x[i-1][j] + dp[i-1][j])%mod
    if j -1 >=0:
      y[i][j] = (y[i][j-1] + dp[i][j-1])%mod
    if i-1>=0 and j-1 >=0:
      z[i][j] = (z[i-1][j-1] + dp[i-1][j-1])%mod
    dp[i][j] += (x[i][j] + y[i][j] + z[i][j])%mod
      
print(dp[h-1][w-1])

      
      