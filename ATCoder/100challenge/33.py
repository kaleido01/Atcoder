# -*- coding: utf-8 -*-
import sys

sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
mapInt = lambda: map(int, input().split())
listInt = lambda: list(map(int, input().split()))

init0 = lambda n: [0 for _ in range(n)]
inithwv = lambda h, w, v: [[v for _ in range(w)] for _ in range(h)]
inithw = lambda h: [ list(input()) for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]

YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1
from operator import itemgetter
from collections import deque


h, w = mapInt()

grid = inithw(h)

black = 0
for i in range(h):
  for j in range(w):
    if grid[i][j] == "#":
      black += 1

que = deque()

done = inithwv(h,w, False)

dx = [-1,0,1,0]
dy = [0,1,0,-1]

que.append((2,0,0))

while(que):
  count, x, y = que.popleft()
  
  for i in range(4):
    sx, sy = x,y
    sx += dx[i]
    sy += dy[i]
    
    if not(0 <= sx < w) or not (0 <= sy < h):
      continue
    
    if sx == w-1 and sy == h-1 :

      print(h * w - count - black)
      sys.exit()
    if done[sy][sx]:
      continue
    if grid[sy][sx] == "#":
      continue
    
    
    done[sy][sx] = True
    que.append((count +1 ,sx, sy))
    
  

print(-1)