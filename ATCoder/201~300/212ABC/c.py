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
init1 = lambda n: [-1 for _ in range(n)]

inithwv = lambda h, w, v: [[v for _ in range(w)] for _ in range(h)]
inithw = lambda h: [ list(input()) for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]
bit = lambda n, k:((n >> k) & 1) # nのkビット目
int1=lambda x:int(x)-1

a, b= mapInt()

p = listInt()
q = listInt()

p.sort()

def isOK(index, v):
  return p[index] >= v

ans = INF
for i in range(b):
  
  left = -1
  right = a
  while(right - left > 1):
    middle = (right + left)// 2
    
    if isOK(middle, q[i]):
      right = middle
    else:
      left = middle
  
  if right == a:
    x = abs(q[i] - p[left])
    ans = min(ans, x)
  else:
    x = abs(q[i] - p[left])
    y = abs(q[i] - p[right])
    ans = min(ans, min(x,y))
    
    
print(ans)