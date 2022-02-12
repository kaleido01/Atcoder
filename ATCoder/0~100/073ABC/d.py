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
inithw = lambda h: [ list(map(int, input().split())) for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]
bit = lambda n, k:((n >> k) & 1) # nのkビット目
# YesNo=lambda b: bool([print('Yes')] if b else print('No'))
# YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

n, m, R = mapInt()
r = listInt()

dp = [[math.inf for  _ in range(n)] for _ in range(n)]
for i in range(m):
  s,t,d = map(int, input().split())
  s -=1
  t -=1
  dp[s][t] = d
  dp[t][s] = d
  

for i in range(n):
    dp[i][i]=0

for k in range(n):
  for i in range(n):
    for j in range(n):
      dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
      
      
for i in range(R):
  r[i] -= 1

patterns = list(itertools.permutations(r, R))
# print(patterns)

ans = INF
for pattern in patterns:
  cost = 0
  for i in range(R-1):
    cur = pattern[i]
    ne = pattern[i+1]
    cost += dp[cur][ne]
  # print(cost)
  ans = min(ans, cost)
  
# print(dp)
print(ans)