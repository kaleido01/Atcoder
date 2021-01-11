# -*- coding: utf-8 -*-
import sys

sys.setrecursionlimit(10**9)
# INF=H * W
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
INF=h * w

sy, sx, gy, gx = mapInt()
sx -= 1
sy -= 1
gx -= 1
gy -= 1

grid = inithw(h)

dist = [ [ [INF for _ in range(w)] for _ in range(h) ] for _ in range(2)]

que = deque()

# "0 tate 1 yoko"
# dx = [0, -1, 0, 1]
# dy = [1, 0, -1, 0]
dxy = [[(0,1),(0,-1)], [(1,0), (-1,0)]]
dist[0][sy][sx] = 0
dist[1][sy][sx] = 0

que.append((0, sx, sy))
que.append((1, sx, sy))

while(que):
  d, x, y = que.popleft()
  # print(x,y)
  for dx,dy in dxy[d]:
    nx = x
    ny = y
    nx += dx
    ny += dy
    
    if x == gx and y == gy:
      print(min(dist[0][y][x],dist[1][y][x]))
      sys.exit()

    if not (0 <= nx < w) or not(0 <= ny < h):
      continue
    
    if grid[ny][nx] == "#":
      continue
    
    if dist[(d+1) % 2][ny][nx] != INF:
      continue
    if dist[(d+1) % 2][ny][nx] > dist[d][y][x] + 1:
      dist[(d+1) % 2][ny][nx] = dist[d][y][x] + 1
      que.append(((d+1) % 2, nx, ny))
    
print(-1)
    
    
    
  