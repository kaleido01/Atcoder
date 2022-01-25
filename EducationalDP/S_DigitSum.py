# -*- coding: utf-8 -*-
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect, statistics
from collections import Counter, defaultdict, deque
from typing import ItemsView
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
# YesNo=lambda b: bool([print('Yes')] if b else print('No'))
# YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

p = input()
n = len(p)
d = int(input())


dp = [[ [0, 0] for _ in range(d)] for _ in range(n+1)]
dp[0][0][0] = 1
for i in range(n):
  # 1~9
  v = int(p[i])
  # print(v)
  # exact -> exact
  for j in range(d):
    nextD = (v + j) % d
    dp[i+1][nextD][0] += dp[i][j][0]
    dp[i+1][nextD][0] %= MOD

  # exact -> Any
  for j in range(d):
    for k in range(v):
      nextD = (k + j) % d
      dp[i+1][nextD][1] += dp[i][j][0]
      dp[i+1][nextD][1] %= MOD

  # Any -> Any
  for j in range(d):
    for k in range(10):
      nextD = (k + j) % d
      dp[i+1][nextD][1] += dp[i][j][1]
      dp[i+1][nextD][1] %= MOD
      

  
# print(dp)
print((dp[n][0][0] + dp[n][0][1]-1)%MOD)
