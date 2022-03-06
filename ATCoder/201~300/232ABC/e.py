# -*- coding: utf-8 -*-
import sys, getpass, string
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
sys.setrecursionlimit(3*10**5+10)
INF=10**18
MOD=998244353 # 998244353
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
input=lambda: sys.stdin.readline().rstrip()
mapInt = lambda: map(int, input().split())
listInt = lambda: list(map(int, input().split()))

init0 = lambda n: [0 for _ in range(n)]
init1 = lambda n: [-1 for _ in range(n)]
initAny = lambda n, a: [a for _ in range(n)]


inithwv = lambda h, w, v: [[v for _ in range(w)] for _ in range(h)]
inithw = lambda h: [ list(input()) for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]
bit = lambda n, k:((n >> k) & 1) # nのkビット目
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
# YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

# n = int(input())
# s = input()
h, w, k = mapInt()
sx, sy, ex, ey = mapInt()

dp = [ [ [ 0 for i in range(2)] for i in range(2)] for i in range(k+1)] 

if sx == ex and sy == ey:
  dp[0][1][1] = 1
elif sx == ex:
  dp[0][1][0] = 1
elif sy == ey:
  dp[0][0][1] = 1
else:
  dp[0][0][0] = 1

for i in range(k):
  for istate in range(2):
    for isyoko in range(2):
      if istate == 1 and isyoko == 1:
        dp[i+1][istate][isyoko] += dp[i][0][1] + dp[i][1][0]
      if istate == 0 and isyoko == 0:
        dp[i+1][istate][isyoko] += (w-1) * dp[i][0][1] + (h-1) * dp[i][1][0] + (h+w-4) *dp[i][0][0]
      if istate == 1 and isyoko == 0:
        dp[i+1][1][0] += dp[i][0][0] + (w-2) * dp[i][1][0] + (w-1) * dp[i][1][1]
      if isyoko == 1 and istate == 0:
        dp[i+1][0][1] += dp[i][0][0] + (h-2) * dp[i][0][1] + (h-1) * dp[i][1][1]
      dp[i+1][istate][isyoko] %= MOD
        
# print(dp)
print(dp[k][1][1])
        
