# -*- coding: utf-8 -*-
import sys

sys.setrecursionlimit(10**9)
INF=10**18
MOD=998244353
input=lambda: sys.stdin.readline().rstrip()
mapInt = lambda: map(int, input().split())
listInt = lambda: list(map(int, input().split()))

init0 = lambda n: [0 for _ in range(n)]
inithwv = lambda h, w, v: [[v for _ in range(w)] for _ in range(h)]
inithw = lambda h: [ list(input()) for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]
bit = lambda n, k:((n >> k) & 1) # nのkビット目
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1
from operator import itemgetter
from collections import deque
import heapq


H, W, K = mapInt()

C = [[ "" for _ in range(W)] for _ in range(H)]

for i in range(K):
  x = list(input().split())
  C[int(x[0]) - 1][int(x[1]) - 1] = x[2]

# 0のときはX 1のときはD 2のときはR
dp = [[[ 0 for _ in range(3)] for i in range(W+1)] for i in range(H+1)]

print(C)
if C[0][0] == "R":
  dp[0][0][2] = 1
elif C[0][0] == "X":
  dp[0][0][0] = 1
elif C[0][0] == "D":
  dp[0][0][1] = 1
else:
  dp[0][0][0] = 1
  dp[0][0][1] = 1
  dp[0][0][2] = 1
    
    
for i in range(H):
  for j in range(W):
    # for k in range(3):

    #下方向の処理
    
    if i != H-1:

      if C[i+1][j] == "":
        dp[i+1][j][0] += (1 if j == W - 1 else 2) * (dp[i][j][0] + dp[i][j][1])
        dp[i+1][j][1] += (1 if j == W - 1 else 2)  * (dp[i][j][0] + dp[i][j][1])
        dp[i+1][j][2] += (1 if j == W - 1 else 2)  * (dp[i][j][0] + dp[i][j][1])
      if C[i+1][j] == "X":
        dp[i+1][j][0] += (dp[i][j][0] + dp[i][j][1])
      if C[i+1][j] == "D":
        dp[i+1][j][1] += (dp[i][j][0] + dp[i][j][1])
      if C[i+1][j] == "R":
        dp[i+1][j][2] += (dp[i][j][0] + dp[i][j][1])
    #右方向の処理
    if j != W-1:
      if C[i][j+1] == "":
        dp[i][j+1][0] += (1 if i == H - 1 else 2)  * (dp[i][j][0] + dp[i][j][2])
        dp[i][j+1][1] += (1 if i == H - 1 else 2)  * (dp[i][j][0] + dp[i][j][2])
        dp[i][j+1][2] += (1 if i == H - 1 else 2)  * (dp[i][j][0] + dp[i][j][2])
      if C[i][j+1] == "X":
        dp[i][j+1][0] += (dp[i][j][0] + dp[i][j][2])
      if C[i][j+1] == "D":
        dp[i][j+1][1] += (dp[i][j][0] + dp[i][j][2])
      if C[i][j+1] == "R":
        dp[i][j+1][2] += (dp[i][j][0] + dp[i][j][2])
          


ans = 0
for i in range(3):
  ans += dp[H-1][W-1][i]
  
print(dp)
print(ans)