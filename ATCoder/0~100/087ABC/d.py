# -*- coding: utf-8 -*-
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
from typing import Deque
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
initAny = lambda n, a: [a for _ in range(n)]


inithwv = lambda h, w, v: [[v for _ in range(w)] for _ in range(h)]
inithw = lambda h: [ list(input()) for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]
bit = lambda n, k:((n >> k) & 1) # nのkビット目
# YesNo=lambda b: bool([print('Yes')] if b else print('No'))
# YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

n, m = mapInt()

g = [ [] for i in range(n)]

for i in range(m):
  l, r, d = mapInt()
  l -= 1
  r -= 1
  
  g[l].append((r, d))
  g[r].append((l, -d))


done = [False] * n
pos = [INF] * n

q = Deque()
for i in range(n):
  if done[i]: continue
  done[i] = True
  q.append(i)
  ok = True
  while(q):
    cpos = q.popleft()
    nodes = g[cpos]
    if pos[cpos] == INF:
      pos[cpos] = 0
    for node in nodes:
      ne, d = node
      if pos[ne] == INF:
        pos[ne] = pos[cpos] + d
      else:
        if pos[ne] != pos[cpos] + d:
          ok = False
      if done[ne]: continue
      done[ne] = True
      q.append(ne)
  if not ok:
    print("No")
    exit()
print("Yes")        
      

  
