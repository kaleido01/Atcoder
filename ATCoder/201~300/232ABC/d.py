# -*- coding: utf-8 -*-
from dis import dis
import sys, getpass, string
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
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
h, w = mapInt()

g = [ list(input()) for _ in range(h)]


q = deque()
dist = [ [ -1 for _ in range(w)] for i in range(h)]
dist[0][0] = 1

q.append((0,0))

dx = [0, 1]
dy = [1, 0]
while(q):
  cx ,cy = q.popleft()
  
  for i in range(2):
    nx = cx + dx[i]
    ny = cy + dy[i]
    # print(nx,ny)
    if not(0 <= nx < w and 0 <= ny < h): continue
    if g[ny][nx] == "#": continue
    if dist[ny][nx] != -1: continue
    dist[ny][nx] = dist[cy][cx] + 1
    
    q.append((nx, ny))


ans = 0
# print(dist, g)
for i in range(h):
  ans = max(ans, max(dist[i]))
  
print(ans)