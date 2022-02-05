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
  a, b = mapInt()
  a -=1
  b -=1
  g[a].append(b)
  g[b].append(a)
  
  
  

done = [False] * n
# def dfs(pos, isFirst):
  
#   nodes = g[pos]
#   cnt = 0
#   for node in nodes:
#     if done[node]: continue
#     done[node] = True
#     if not isFirst:
#       cnt +=1
    
#     cnt += dfs(node, False)
    
#   return cnt
  
  
  
q = deque()
for i in range(n):
  done = [False] * n
  done[i] = True
  for node in g[i]:
    done[node] = True
    q.append(node)
  ans = 0
  while(q):
    pos = q.popleft()
    nodes = g[pos]
    for node in nodes:
      if done[node]: continue
      done[node] = True
      ans +=1
      
    
  print(ans)