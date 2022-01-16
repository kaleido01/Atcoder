# -*- coding: utf-8 -*-
import sys, getpass
import math, random
from math import factorial
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
from typing import Iterable, Tuple
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


n, h = mapInt()
katana = []

ma = 0
for i in range(n):
  a, b = mapInt()
  ma = max(ma, a)
  katana.append(b)
  
  
katana.sort(reverse= True)

ans = 0
isEnd = False
for v in katana:
  if ma >= v:
    if h % ma == 0:
      ans += h // ma
    else:
      ans += h // ma + 1
    isEnd = True
    break
  else:
    h -= v
    ans +=1
    if h <= 0:
      isEnd = True
      break
if not isEnd:
    if h % ma == 0:
      ans += h // ma
    else:
      ans += h // ma + 1
print(ans)