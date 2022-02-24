# -*- coding: utf-8 -*-
from audioop import lin2adpcm
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

n, a, b, c = mapInt()
l = []
for i in range(n):
  l.append(int(input()))

patterns = list(itertools.permutations(l, n))

ans = INF
for p in patterns:
  for i in range(1,n-1):
    for j in range(i+1, n):
      for k in range(j+1, n+1):
        # print(p)
        s = p[: i]
        t = p[i: j]
        u = p[j: k]
        temp = 0
        temp += 10 * (len(s)-1)
        temp += 10 * (len(t)-1)
        temp += 10 * (len(u)-1)
        # print(s,t,u)
        s = sum(s)
        t = sum(t)
        u = sum(u)
        # print(s,t,u)
        temp += abs(a-s)
        temp += abs(t-b)
        temp += abs(u-c)
        ans = min(ans, temp)
      
print(ans)
      