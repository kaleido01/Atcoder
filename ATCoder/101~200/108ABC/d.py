# -*- coding: utf-8 -*-
from genericpath import isfile
from re import L
import sys, getpass, string
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
from types import TracebackType
sys.setrecursionlimit(3*10**5+10)
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
n, x, y = mapInt()
x -= 1
y -= 1
g = [ [] for i in range(n)]
done = [ [ INF for i in range(n) ]for i in range(n)]


for i in range(n-1):
  g[i].append(i+1)
  g[i+1].append(i)

g[x].append(y)
g[y].append(x)
# print(g)
  
  
ans = [0] * (n-1)
for i in range(n):
  dist = [-1] * n
  q = deque()
  q.append(i)
  dist[i] = 0
  # isfirst = True
  while(q):
    pos = q.pop()
    
    nodes = g[pos]
    
    for node in nodes:
      if dist[node] == -1:
        dist[node] = dist[pos] + 1
        q.append(node)
      else:
        if dist[node] > dist[pos] + 1:
          dist[node] = dist[pos] + 1
          q.append(node)
        
      
  
  # print(dist)
  for j in range(n):
    if dist[j] != -1 and dist[j] != 0:
      # ans[dist[j]-1] += 1
      done[i][j] = min(dist[j], done[i][j], done[j][i])
      done[j][i] = min(dist[j], done[j][i], done[i][j])
      
      

dist= [0]*(n-1)
for i in range(n-1):
  for j in range(i+1, n):
    # print(done[i][j])
    dist[done[i][j]-1] +=1
print(*dist)