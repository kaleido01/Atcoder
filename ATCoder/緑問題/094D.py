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

an = listInt()

an.sort()

m = an[-1]

r = m // 2
ans = 0
index = 0
isOK = False
for i in range(n-1):
  if an[i] > r:
    index = i
    if abs(an[i] - r) > abs(an[i-1]-r):
      ans = an[i-1]
    else:
      ans = an[i]
    isOK = True
    break

if isOK:
  print(m, ans)
else:
  print(m, an[-2])
  