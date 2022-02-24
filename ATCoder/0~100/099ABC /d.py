# -*- coding: utf-8 -*-
from http.client import OK
from pickle import TRUE
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
from typing import Deque
INF=10**18
MOD=10**9+7 # 998244353
d4 = [(1,0),(0,1),(-1,0),(0,-1)]
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

n, C = mapInt()

d = [ listInt() for i in range(C)]

grid = [ listInt() for i in range(n)]


s = [ [0 for i in range(3)] for i in range(C)]

for c in range(C):
  for i in range(n):
    for j in range(n):
      now = grid[i][j]
      change = d[now-1][c]
      s[c][(i+1+j+1) % 3] += change
      

l = [ i for i in range(C)]
c_list = list(itertools.permutations(l, 3))

ans = INF
for lis in c_list:
  p, q, r = lis
  
  ans = min (ans, s[p][0] + s[q][1] + s[r][2])
print(ans)
  
  