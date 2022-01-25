# -*- coding: utf-8 -*-
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
from typing import Deque
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7 # 998244353
d4 = [(1,0),(0,1),(-1,0),(0,-1)]
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

ch, cw = mapInt()
ch -= 1
cw -= 1

dh, dw = mapInt()
dh -= 1
dw -= 1


s = [list(input()) for _ in range(h)]
# print(s)
que = Deque()

done = [[False for _ in range(w)] for _ in range(h)]
dist = [[-1 for _ in range(w)] for _ in range(h)]
dist[ch][cw] = 0
que.append((ch, cw))


while que:
  cy, cx = que.popleft()
  # if cy == dh and cx == dw:
  #   break
  
  # 上下左右
  for dx, dy in d4:
    ny = cy + dy
    nx = cx + dx
    # print(ny,nx)
    if not (0 <= ny < h and 0 <= nx < w): continue
    if s[ny][nx] == "#": continue
    
    if dist[ny][nx] == -1 or dist[ny][nx] > dist[cy][cx]:
      dist[ny][nx] = dist[cy][cx]
      # done[ny][nx] = True
      que.appendleft((ny, nx))
    
    
   #テレポート 
  for i in range(-2, 3):
    for j in range(-2, 3):
      ny = cy + i
      nx = cx + j
      
      if not(0 <= ny < h and 0 <= nx < w): continue
      if s[ny][nx] == "#": continue
      
      if dist[ny][nx] == -1:
        dist[ny][nx] = dist[cy][cx] + 1
        # done[ny][nx] = True
        que.append((ny, nx))

    
# print(dist)
print(dist[dh][dw])