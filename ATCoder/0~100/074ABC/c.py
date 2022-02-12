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


A, B, C, D, E, F = mapInt()

mass = 0
sugar = 0
p = 0

for a in range(F//(A)+10):
  for b in range(F//(B)+10):
    # print(a, b)
    if a==b==0: continue
    if 100*a*A + 100*b*B > F: continue
    now = F - 100*a*A - 100*b*B
    for c in range(0, now+10, C):
      for d in range(0, now+10, D):
        if 100*a*A + 100*b*B + c+d > F: continue
        if (a*A+b*B)*E < c+d: continue
        temp = (c + d) / (100*a*A + 100*b*B + c + d)
        if temp >= p:
          p = temp
          mass = 100*a*A + 100*b*B + c+d
          sugar = c+d
print(mass, sugar)