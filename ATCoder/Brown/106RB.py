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

n, m = mapInt()

a = listInt()
b = listInt()

grid = [[] for _ in range(n)]

for i in range(m):
  c, d = mapInt()
  c -= 1
  d -= 1
  grid[c].append(d)
  grid[d].append(c)

done = [False] * n


def dfs(pos, cur):
  ca = a[pos]
  cb = b[pos]
  cur += cb - ca
  nodes = grid[pos]
  
  for node in nodes:
    if done[node]: continue
    done[node] = True
    cur += dfs(node, 0)
  
  return cur
  

yes = True
for i in range(n):
  if done[i]: continue
  done[i] = True
  
  cur = dfs(i, 0)
  if cur != 0:
    yes = False
    
YesNo(yes)