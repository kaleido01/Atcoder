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

a = [0] * m
b = [0] * m

for i in range(m):
  p, q = mapInt()
  a[i] = p -1
  b[i] = q -1


k = int(input())

c = [0] * k
d = [0] * k


for i in range(k):
  p, q = mapInt()
  c[i] = p - 1
  d[i] = q - 1
  
ans = 0
for i in range(1 << k):
  res = 0
  put = []
  for j in range(k):
    if (i >> j) & 1:
      put.append(c[j])
    else:
      put.append(d[j])
  for x in range(m):
    if a[x] in put and b[x] in put:
      res +=1
  
  ans = max(ans, res)

print(ans)