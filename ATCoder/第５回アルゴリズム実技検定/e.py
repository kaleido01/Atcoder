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


h, w = mapInt()

grid = inithw(h)

hanko = inithw(h)

hankoGrid = []

cover = max(h,w)
for i in range(h):
  for j in range(w):
    if hanko[i][j] == "#":
      hankoGrid.append((j,i))


for rotate in range(4):
  if rotate != 0:
    grid = list(zip(*grid[::-1]))
  if rotate == 1 or rotate ==3:
    h,w = w,h
  elif rotate == 2:
    h,w = w,h
  # print(grid,h,w)
  
  for i in range(-1 * cover, cover):
    for j in range(-1 * cover, cover):
      canFit = True
      for v in hankoGrid:
        vx,vy = v
        vx += j
        vy += i
        if not ( 0 <= vx < w) or not(0 <= vy < h):
          canFit = False
          break
        if grid[vy][vx] == "#":
          canFit = False
          break
      if canFit:
        print("Yes")
        sys.exit()
        
        
print("No")