# -*- coding: utf-8 -*-
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
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
inithwv = lambda h, w, v: [[v for _ in range(w)] for _ in range(h)]
inithw = lambda h: [ list(input()) for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]
bit = lambda n, k:((n >> k) & 1) # nのkビット目
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

n,m = mapInt()

x = []
y = []
z = []

for i in range(n):
  a, b, c = mapInt()
  x.append(a)
  y.append(b)
  z.append(c)
  

# def s(x, y, z):
#   return abs(x) + abs(y) + abs(z)

ans = -INF
for a in range(-1, 2, 1):
  for b in range(-1, 2, 1):
    for c in range(-1, 2, 1):
      if a == 0 or b == 0 or c == 0: continue
      dp = [ [ -INF for _ in range(m+2) ] for _ in range(n+1)]
      dp[0][0] = 0
      for i in range(n):
        for j in range(m+1):
          d = a*x[i] + b*y[i] + c*z[i]
          dp[i+1][j] = max(dp[i+1][j], dp[i][j])
          dp[i+1][j+1] = max(dp[i][j+1], dp[i][j] + d)
      # print(dp)
      ans = max(ans, dp[n][m])
    
    
    
print(ans)

