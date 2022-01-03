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
init1 = lambda n: [-1 for _ in range(n)]

inithwv = lambda h, w, v: [[v for _ in range(w)] for _ in range(h)]
inithw = lambda h: [ list(input()) for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]
bit = lambda n, k:((n >> k) & 1) # nのkビット目
# YesNo=lambda b: bool([print('Yes')] if b else print('No'))
# YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

# h, w = mapInt()
n = int(input())
a =[]
for i in range(n):
  a.append(listInt())

m = int(input())

ng = inithwv(n+1,n+1,False)

# print(a)

for i in range(m):
  x, y = mapInt()
  ng[x][y] = True
  ng[y][x] = True
  
# print(ng)
runner = init0(n+1)
all = list(itertools.permutations([i for i in range(n)]))
ans = INF
ok = False
for v in all:
  
  time = 0
  canGoal = True
  for i in range(n):
    now = v[i]
    if i < n-1:
      next = v[i+1]
      # print(v, now, next, canGoal,ng[now+1][next+1])
      if (ng[now+1][next+1]):
        canGoal = False
        break
    time += a[now][i]
  if canGoal:
    ans = min(ans, time)
    ok = True

if ok:
  print(ans)
else:
  print("-1")
    
      




m = 1001
