# -*- coding: utf-8 -*-
import re
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
n = int(input())

v = listInt()

x = {-1:0}
y = {-1:0}

for i in range(n):
  if i % 2 == 0:
    if v[i] in x:
      x[v[i]] +=1
    else:
      x[v[i]] = 1
  if i % 2 == 1:
    if v[i] in y:
      y[v[i]] +=1
    else:
      y[v[i]] = 1


sortX = sorted(x.items(), reverse=True, key=lambda p: p[1])
sortY = sorted(y.items(), reverse=True, key=lambda p: p[1])

# print(sortX, sortY)
if sortX[0][0] == sortY[0][0]:
  
  v1 = sortX[1][1]
  v2 = sortY[1][1]
  ans = min(n- sortX[0][1]-v2, n-v1-sortY[0][1])
  print(ans)
    
else:
  # half = n // 2
  ans = n - sortX[0][1] - sortY[0][1]
  print(ans)