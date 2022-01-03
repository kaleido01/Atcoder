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
inithw = lambda h: [ list(input()) for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]
bit = lambda n, k:((n >> k) & 1) # nのkビット目
# YesNo=lambda b: bool([print('Yes')] if b else print('No'))
# YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

n, m = mapInt()
g = initDp(n)

for i in range(m):
  a, b = mapInt()
  a, b = a-1, b-1
  g[a].append(b)
  g[b].append(a)
  

# done = [False for _ in range(n)]
# def dfs(pos, pre, count):
#   done
#   for nv in g[pos]:
#     if nv != pre:
#         if len(g[pos]) and pos - 1 == nv:
#           count += 1
          
#           count += dfs(nv, pos, count)
#   return count
          
ans = 0
for i in range(n):
  edges = g[i]
  count = 0
  for j in edges:
    if i > j:
      count += 1
  if count == 1:
    ans += 1
          
print(ans)
          
          
    