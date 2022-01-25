# -*- coding: utf-8 -*-
from ast import Mod
from ctypes import Union
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
from tokenize import group
from typing import Deque
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

edges = [ [] for _ in range(n)] 
dp = [0] * n
deps = [-1] * n
done = [False] * n


for i in range(m):
  a, b = mapInt()
  a -= 1
  b -= 1
  edges[a].append(b)
  edges[b].append(a)
  
  
  
que = Deque()
dp[0] = 1
deps[0] = 0
que.append((0,-1, 0))

while(que):
  pos, pre, cnt = que.popleft()

  for node in edges[pos]:
    if node == pre: continue
    #その回数+1が最短での移動回数
    
    if deps[node] == -1:
      deps[node] = cnt
    if deps[node] == cnt:
       dp[node] += dp[pos]
    else:
      continue
    if done[node]: continue
    done[node] = True
    que.append((node, pos, cnt + 1))
    
# print(dp, deps)
print(dp[n-1] % MOD)
