# -*- coding: utf-8 -*-
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
from time import time
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

# h, w = mapInt()
# n = int(input())

n, m = mapInt()

g = [ [] for _ in range(n)]

done = {}
for i in range(m):
  u, v = mapInt()
  u -=1
  v -=1
  g[u].append(v)
  # done[(u, v, 0)] = -1
  # done[(u, v, 1)] = -1
  # done[(u, v, 2)] = -1
  
S, T = mapInt()
S -=1
T -=1


q = deque()
q.append((S,1))
done[(S,0)] = 0
while(q):
  pos, v = q.popleft()
  nodes = g[pos]
  for node in nodes:
    # print((node, v))
    if (node,v) in done: continue
    # print("next")
    if v == 0:
      done[(node,v)] = done[(pos, 2)] + 1
    else:
      done[(node,v)] = done[(pos, v-1)] + 1
    q.append((node, (v+1)%3))

# print(done)
if (T,0) in done:
  print(done[(T, 0)] // 3)
else:
  print(-1)
  