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
# YesNo=lambda b: bool([print('Yes')] if b else print('No'))
# YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

h, w = mapInt()
grid = []
for i in range(h):
  
  grid.append(listInt())

ans = 0

for i in range(2 ** h):
  value = [0] * (h * w + 1)
  cs = []

  for j in range(h):
    if (i >> j) & 1:
      cs.append(grid[j])
  for j in range(w):
    isSame = True
    if len(cs) == 0:
      break
    elif len(cs) == 1:
      for k in range(len(cs)):
        value[cs[k][j]] += 1
    else:
      for k in range(len(cs)-1):
        if cs[k][j] != cs[k+1][j]:
          isSame = False
      if isSame:
        value[cs[k][j]] +=1
  m = max(value)
  # print(cs, m)
  ans = max(ans, m * len(cs))
    
print(ans)
  
