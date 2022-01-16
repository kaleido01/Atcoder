# -*- coding: utf-8 -*-
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7 # 998244353
d4 = [(0,1), (1,0)]
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


h, w = mapInt()


grid = []

for i in range(h):
  grid.append(listInt())
  

# print(grid)
ans = 0
arr = []

for i in range(h):
  for j in range(w):
    v = grid[i][j]
    if v % 2 == 0: continue
    
    for dx, dy in d4:
      cx = j + dx
      cy = i + dy
      if not(0 <= cy < h and 0 <= cx < w): continue
      # if grid[cy][cx] % 2 == 1:
      ans +=1
      arr.append((i+1, j+1, cy+1, cx+1))
      grid[i][j] -=1
      grid[cy][cx] +=1
      
      break
      # else:
      #   ans +=1
      #   arr.append((i, j, cy, cx))
        
      
      
print(ans)
for i in range(ans):
  print(*arr[i])
  
