# -*- coding: utf-8 -*-
import sys, getpass, string
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
sys.setrecursionlimit(3*10**5+10)
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
# h, w = mapInt()
v, e = mapInt()

x=[]
dp = [[math.inf for  _ in range(v)] for i in range(v)]
for i in range(e):
  s,t,d = map(int, input().split())
  s -=1
  t -=1
  dp[s][t] = d
  dp[t][s] = d
  x.append((s,t,d))
  
for i in range(v):
    dp[i][i] = 0

for k in range(v):
  for i in range(v):
    for j in range(v):
      dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
      

ans = 0
for i in range(e):
  a, b, c = x[i]
  for middle in range(v):
    if a == middle or b == middle: continue
    
    if dp[a][middle] + dp[middle][b] <= c:
      ans +=1
      break

print(ans)