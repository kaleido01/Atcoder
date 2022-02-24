# -*- coding: utf-8 -*-
import sys, getpass, string
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
initAny = lambda n, a: [a for _ in range(n)]


inithwv = lambda h, w, v: [[v for _ in range(w)] for _ in range(h)]
inithw = lambda h: [ list(input()) for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]
bit = lambda n, k:((n >> k) & 1) # nのkビット目
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
# YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

# n = int(input())
# s = input()
# h, w = mapInt()
n = int(input())
g = [ [] for _ in range(n)]
for i in range(n-1):
  u, v = mapInt()
  u -= 1
  v -= 1
  g[u].append(v)
  g[v].append(u)
  
  
ans = [ [] for _ in range(n)]


# leaf = [1]
leaf = 1
def dfs(pre, pos):
  global leaf
  nodes = g[pos]
  
  # 自分しかいけないのでout
  if pre != -1 and len(nodes) == 1:
    ans[pos] = (leaf, leaf)
    leaf +=1
    return ans[pos]
  
  ml = INF
  mr = -INF
  for node in nodes:
    if node == pre: continue
    x, y = dfs(pos, node)
    ml = min(ml, x)
    mr = max(mr, y)
  ans[pos] = (ml, mr)
  return ans[pos]

  

dfs(-1, 0)
for i in range(n):
  print(*ans[i])