import math
import sys
h ,w = map(int, input().split())


a = [list(map(int ,input().split())) for _ in range(h)]
b = [list(map(int ,input().split())) for _ in range(h)]


m = 80 * (h+w) + 5
# m = 200
dp =[[[False for _ in range(m)] for _ in range(w)] for _ in range(h)]

dp[0][0][abs(a[0][0]-b[0][0])] = True


for i in range(h):
  for j in range(w):
    for k in range(m):
      if dp[i][j][k]:
        if i == h-1 and j == w-1: continue
        elif i == h-1:
          y = abs(a[i][j+1]-b[i][j+1])
          dp[i][j+1][abs(k - y)] =True
          dp[i][j+1][k + y] =True
        elif j == w-1:
          x = abs(a[i+1][j]-b[i+1][j])
          dp[i+1][j][abs(k - x)] =True
          dp[i+1][j][k + x] =True
        else:
          x = abs(a[i+1][j]-b[i+1][j])
          y = abs(a[i][j+1]-b[i][j+1])
          if k - x >=0:
            dp[i+1][j][k - x] =True
          if k - y >= 0:
            dp[i][j+1][k - y] =True
          dp[i+1][j][k + x] =True
          dp[i][j+1][k + y] =True
        
# print(dp[h-1][w-1])
for k in range(m):
  if dp[h-1][w-1][k]:
    print(k)
    sys.exit()