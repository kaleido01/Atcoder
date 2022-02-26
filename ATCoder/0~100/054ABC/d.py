# -*- coding: utf-8 -*-
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
sys.setrecursionlimit(10**9)
INF=500
MOD=10**9+7 # 998244353
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
# YesNo=lambda b: bool([print('Yes')] if b else print('No'))
# YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

# h, w = mapInt()
n, ma, mb = mapInt()

med = []
for i in range(n):
  med.append(listInt())

maxMass = 10 * n + 10


dp = [ [ [ INF for _ in range(maxMass)] for _ in range(maxMass)] for _ in range(n+1)]

dp[0][0][0] = 0

for i in range(n):
  for a in range(maxMass):
    for b in range(maxMass):
      ax, bx, cost = med[i]
      print(a-ax, b-bx, i)
      dp[i+1][a][b] = dp[i][a][b]
      if a-ax >= 0 and b-bx>=0 and dp[i][a-ax][b-bx] != INF:
        dp[i+1][a][b] = min(dp[i][a-ax][b-bx] + cost, dp[i+1][a][b])
        
ans = INF
cnt = 1
while(ma <= maxMass and mb <= maxMass):
    ans = min(ans, dp[n][ma*cnt][mb*cnt])
    cnt +=1
    
    
# print(dp)
if ans == INF:
  print(-1)
else:
  print(ans)