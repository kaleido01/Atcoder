# -*- coding: utf-8 -*-
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


h, w, n = mapInt()

# a = [0] * n
# x = [0] * n
# y = [0] * n

grid = [ [ "" for  _ in range(w)]for i in range(h)]
ans = [ [ -1 for  _ in range(w)]for i in range(h)]
q = deque()
for i in range(n):
  s, t, u = list(input().split())
  q.append([s, int(t) -1, int(u) -1,1])
  grid[int(u) -1][int(t) -1] = s
  ans[int(u) -1][int(t) -1] = 0







now = 0
while(q):
  s, t, u, count = q.popleft()
  # now = max(now, count)
  
  for d in d4:
    sx = t + d[0]
    sy = u + d[1]
    
    if not(0<= sx < w) or not(0 <= sy < h):
      continue

    if grid[sy][sx] != "" and ans[sy][sx] == count and grid[sy][sx] != s:
      grid[sy][sx] = "?"
      continue
    if grid[sy][sx] == "" and ans[sy][sx] == -1:
      grid[sy][sx] = s
      ans[sy][sx] = count
      q.append([s, sx, sy, count + 1])
      
print(ans)
for i in range(h):
  s = ""
  for j in range(w): 
    s += grid[i][j]
  print(s)

    
    
    
    
    
  
  
  

  