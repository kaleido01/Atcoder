# -*- coding: utf-8 -*-
from mailbox import MH
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect, statistics
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
inithw = lambda h: [ list(map(int, input().split())) for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]
bit = lambda n, k:((n >> k) & 1) # nのkビット目
# YesNo=lambda b: bool([print('Yes')] if b else print('No'))
# YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1
#初期化として考えられる最大のnを入力nCr


h, w = mapInt()

ans = INF
# hの全探索
for i in range(1, h):
  A = i * w
  B = (h-i) * (w//2)
  C = (h-i) * (w-w//2)
  ans = min(ans, max(A,B,C) - min(A,B,C))
  D = ((h-i) // 2) * w
  E = ((h-i) - ((h-i) // 2)) * w
  ans = min(ans, max(A,D,E) - min(A,D,E))
  
for i in range(1, w):
  A = i * h
  B = (w-i) * (h//2)
  C = (w-i) * (h-h//2)
  ans = min(ans, max(A,B,C) - min(A,B,C))

  D = ((w-i) // 2) * h
  E = ((w-i) - ((w-i) // 2)) * h
  ans = min(ans, max(A,D,E) - min(A,D,E))
  
print(ans)