# -*- coding: utf-8 -*-
from lib2to3.pgen2.token import INDENT
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


n = int(input())

t = []
a = []

for i in range(n):
  x, y = mapInt()
  t.append(x)
  a.append(y)
  
  
minT = t[0]
minA = a[0]
for i in range(1, n):
  x, y = t[i], a[i]
  
  p = minT // x
  if minT % x != 0:
    p +=1
  q = minA // y
  if minA % y != 0:
    q +=1
  if p == 1 and q == 1:
    minT = x
    minA = y
  else:
    minT = x * max(p,q)
    minA = y * max(p,q)

print(minA+minT)

      