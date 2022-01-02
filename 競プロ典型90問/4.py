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
initx = lambda n, x: [x for _ in range(n)]
inithwv = lambda h, w, v: [[v for _ in range(w)] for _ in range(h)]
inithw = lambda h: [ list(input()) for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]
bit = lambda n, k:((n >> k) & 1) # nのkビット目
# YesNo=lambda b: bool([print('Yes')] if b else print('No'))
# YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

n = intInput()

# n, m = mapInt()

node = initDp(n)
for i in range(n-1):
  a, b = mapInt()
  a, b = a-1, b-1
  node[a].append(b)
  node[b].append(a)
  # node[b] = a
  

# print(node)
# 木の根元を返す
# def dfs(currentNode, length):
#   nextNode = node[currentNode]
#   while nextNode != -1:
#     return dfs(nextNode, length + 1)
#   return (currentNode, length)
  
# bottom, length = dfs(1, 0)
# print(bottom, length)
# bottom, ans = dfs(bottom, 0)

# print(ans+1)


def dfs(s):
  #頂点sからの距離
  dist = [-1] * n
  dist[s] = 0
  
  st = [s]
  while st:
    v = st.pop()
    for nv in node[v]:
      if dist[nv] == -1:
        st.append(nv)
        dist[nv] = dist[v]+1
  
  return dist


dist0 = dfs(0)
mv = max(enumerate(dist0), key= lambda x: x[1])[0]
ans = dfs(mv)
print(max(ans) + 1)

