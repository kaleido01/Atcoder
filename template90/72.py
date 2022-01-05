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

h, w = mapInt()

maze =  inithw(h)
# print(maze)

dx = [-1,0,1,0]
dy= [0,1,0,-1]
def dfs(start, pos,count = 1):
  x, y = pos
  originalX, originalY = start
  # print(x,y, count, ok)
  result = -1
  # hasNext = False
  for i in range(4):
    sx,sy = x,y
    sx += dx[i]
    sy += dy[i]
    if not (0<= sx < w) or not (0<= sy < h):
      continue
    if maze[sy][sx] == "#":
      continue
    if sx == originalX and sy == originalY and count >= 3:
      result = max(result, count)
      continue
    if done[sy][sx]:
      continue
    
    done[sy][sx] = True
    
    value = dfs(start, (sx,sy), count + 1)
    done[sy][sx] = False

    if value != -1:
      result = max(result, value, count)
    
  return result

ans = -1
for i in range(h):
  for j in range(w):
    if maze[i][j] == ".":
      done = [[ False for i in range(w)] for i in range(h)]
      done[i][j] = True
      result = dfs((j,i),(j,i))
      # print(result)
      ans = max(ans, result)

      # if ok:
      #   ans = max(ans, result)
      # else:
      #   print(-1)


print(ans)
  