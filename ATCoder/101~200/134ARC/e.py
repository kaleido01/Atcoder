# -*- coding: utf-8 -*-
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect, statistics
from collections import Counter, defaultdict, deque
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7 # 998244353
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
input=lambda: sys.stdin.readline().rstrip()
mapInt = lambda: map(int, input().split())
listInt = lambda: list(map(int, input().split()))

init0 = lambda n: [0 for _ in range(n)]
init1 = lambda n: [-1 for _ in range(n)]

inithwv = lambda h, w, v: [[v for _ in range(w)] for _ in range(h)]
inithw = lambda h: [ list(input()) for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]
bit = lambda n, k:((n >> k) & 1) # nのkビット目
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
# YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

h, n = mapInt()

m = [ listInt() for i in range(n)]

dp = [ [ INF for i in range(h+1)] for _ in range(n+1)]
for i in range(n+1):
  dp[i][h] = 0

for i in range(1, n+1):
  d, cost = m[i-1]
  for j in range(h, 0, -1):
    jj = max(0, j-d)
    # print(dp[i][j])
    # if j == 0:
    #   dp[i][0] = min(dp[i-1][0], dp[i][0])
    #   continue
    dp[i][j] = min(dp[i-1][j], dp[i][j])
    if dp[i][j] != INF:
     dp[i][jj] = min(dp[i][jj], dp[i-1][jj], dp[i][j] + cost)
    else:
      continue
      # if dp[i-1][j] != INF:=./
      #   dp[i][jj] = min(dp[i-1][jj], dp[i][j] + cost)
      # else:
      # dp[i][jj] = dp[i-1][jj]
      
    
# print(dp)
print(dp[n][0])