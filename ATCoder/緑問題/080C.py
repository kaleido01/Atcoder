# -*- coding: utf-8 -*-
import sys, getpass
import math, random
from math import factorial
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
from typing import Iterable
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7 # 998244353
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
input=lambda: sys.stdin.readline().rstrip()
intInput = lambda: int(input())
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

f = []
for i in range(n):
  f.append(listInt())
  
p = []
for i in range(n):
  p.append(listInt())
  

ans = -INF
for i in range(1, 2**10):
  money = 0
  for k in range(n):
    coOpen = 0
    for j in range(5):
      # if (i >> 2 * j) & 0 and (i >> (2 * j + 1)) & 0: continue
      # j番目の時間帯に店を開く
      if (i >> 2 * j) & 1 and f[k][2*j]:
        coOpen += 1
      if (i >> (2 * j+1)) & 1 and f[k][2*j+1]:
        coOpen += 1
    # print(coOpen)
    money += p[k][coOpen]

  ans = max(ans, money)

print(ans)
