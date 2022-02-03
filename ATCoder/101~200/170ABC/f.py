# -*- coding: utf-8 -*-
import sys
import queue
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
mapInt = lambda: map(int, input().split())
listInt = lambda: list(map(int, input().split()))

init0 = lambda n: [0 for _ in range(n)]
inithwv = lambda h, w, v: [[v for _ in range(w)] for _ in range(h)]
inithw = lambda h, w: [ listInt() for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]

YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1
from operator import itemgetter

h, w, k = mapInt()

x1, y1, x2, y2 = mapInt()

x1 -=1
y1 -=1
x2 -=1
y2 -=1

grid = inithw(h,w)
checked =[[False for _ in range(w)] for _ in range(h)]


que = queue()

count = 1
que.append([x1,y1,count])
checked[x1][y1] = True


dx = [0,1,0,-1]
dy = [-1,0,1,0]


while(que > 0):
  x,y,count = que.popleft()
  # print(x,y,count)
  for i in range(4):
    sx, sy = x,y
    sx += dx[i]
    sy += dy[i]
    if sx == w-1 and sy == h-1:
      print(count+1)
      isOK = True
      break
    # if not (0<= x < w) or not (0<= y < h):
    #   continue
    if checked[sy][sx] == True:
      continue
    checked[sy][sx] = True
    que.append([sx,sy,count+1])

