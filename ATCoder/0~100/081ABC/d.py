# -*- coding: utf-8 -*-
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

n = int(input())
a = listInt()

maxA= -INF
minA = INF
for i in range(n):
  maxA = max(maxA, a[i])
  minA = min(minA, a[i])
  
# All -
if maxA <= 0:
  print(n-1)
  for i in range(n, 1, -1):
    print(i,i-1)
elif minA >= 0:
  print(n-1)
  for i in range(1, n):
    print(i,i+1)
else:
  print(2*n-1)
  if abs(maxA) >= abs(minA):
    target = -1
    for i in range(n):
      if a[i] == maxA:
        target = i+1
    for i in range(1,n+1):
      print(target, i)
    
    for i in range(1, n):
      print(i,i+1)
  else:
    target = -1
    for i in range(n):
      if a[i] == minA:
        target = i+1
    for i in range(1,n+1):
      print(target, i)
    for i in range(n, 1, -1):
      print(i,i-1)