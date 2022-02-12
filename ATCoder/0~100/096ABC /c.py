# -*- coding: utf-8 -*-
from operator import mod
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7 # 998244353
d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
input=lambda: sys.stdin.readline().rstrip()
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

h, w = mapInt()

g = [ list(input()) for i in range(h)]


done = [[ False for i in range(w)] for i in range(h)]



q = deque()
for i in range(h):
  for j in range(w):
    if done[i][j]: continue
    if g[i][j] == "#":
      if (i+1 < h and g[i+1][j] == "#") or (j+1 < w and g[i][j+1] == "#"):
        done[i][j] = True
        q.append((i,j))
      else:
        print("No")
        exit()
    while q:
      cx, cy = q.popleft()
      
      for dx, dy in d4:
        nx, ny = cx+dx, cy+dy
        if not(0<=nx< h and 0<=ny < w):continue
        if g[nx][ny] != "#":continue
        if done[nx][ny]: continue
        
        
        done[nx][ny] = True
        q.append((nx,ny))


print("Yes")

        
      