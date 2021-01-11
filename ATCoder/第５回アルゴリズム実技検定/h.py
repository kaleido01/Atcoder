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
inithw = lambda h: [ list(input())for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]

YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1
from operator import itemgetter
from itertools import combinations, permutations, combinations_with_replacement
from collections import deque

h, w = mapInt()
r, c = mapInt()
r -=1
c -=1

grid = inithw(h)
done = [[False for i in range(w)] for i in range(h)]
ans = [["x" for i in range(w)] for i in range(h)]
que = deque()


      
dx = [0, 1 ,0 ,-1]
dy = [1, 0, -1 ,0]

que.append([r, c])
done[r][c] = True
ans[r][c] = "o"


while(len(que)>0):
  x, y = que.popleft()
  for i in range(4):
    sx, sy = x,y
    sx += dx[i]
    sy += dy[i]
    # print(sx,sy,i)
    if not(0 <= sx < h) or not(0 <= sy < w):
      continue

    if grid[sx][sy] =="#":
      ans[sx][sy] = "#"
      continue
    
    if done[sx][sy]:continue
      
    
    if grid[sx][sy] == "<" and i == 0:
      done[sx][sy] = True
      que.append([sx, sy])
      ans[sx][sy] = "o"
    elif grid[sx][sy] == "^" and i == 1:
      done[sx][sy] = True
      que.append([sx, sy])
      ans[sx][sy] = "o"
    elif grid[sx][sy] == "v" and i == 3:
      done[sx][sy] = True
      que.append([sx, sy])
      ans[sx][sy] = "o"
    elif grid[sx][sy] == ">" and i == 2:
      done[sx][sy] = True
      que.append([sx, sy])
      ans[sx][sy] = "o"
    elif grid[sx][sy] == ".":
      done[sx][sy] = True
      que.append([sx, sy])
      ans[sx][sy] = "o"
  
    
    
    
    
for i in range(h):
  for j in range(w):
    if grid[i][j] =="#":
      ans[i][j] ="#"

for i in range(h):
  print("".join(ans[i]))
  
  