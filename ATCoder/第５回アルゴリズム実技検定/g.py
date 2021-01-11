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

grid = inithw(h)

snake = 0
snakeQue = []
ansSnake = []

que = deque()


      
dx = [0, 1 ,0 ,-1]
dy = [1, 0, -1 ,0]

for i in range(h):
  for j in range(w):
    if grid[i][j] == "#":
      snake += 1
      snakeQue.append([i,j])
      
      
while(len(snakeQue)>0):
  # ans =[]
  # done = [[False for i in range(w)] for i in range(h)]
  p, q = snakeQue.pop(0)
  # done[p][q] = True
  que.append([p, q, [[p,q]]])
  # print(que)

  while(len(que)>0):
    x, y, ans = que.popleft()
    # print(ans)
    if len(ans) == snake:
      ansSnake = ans
      # print(ans)
      break
    for i in range(4):
      sx, sy = x,y
      newAns = ans.copy()
      sx += dx[i]
      sy += dy[i]
      
      if not(0 <= sx < h) or not(0 <= sy < w):
        continue
      # if grid[sx][sy] =="." or done[sx][sy]:
      #   continue
      if grid[sx][sy] ==".":
        continue
      isOK = True
      for j in range(len(newAns)):
        if sx == newAns[j][0] and sy == newAns[j][1]:
          isOK = False
          break
      if not isOK:continue
      # done[sx][sy] = True
      newAns.append([sx,sy])
      # print(newAns)
      que.append([sx,sy,newAns])
      # ans.append([sx+1,sy+1])
  if len(ansSnake) == snake:
    break
  
print(len(ansSnake))
for i in range(len(ansSnake)):
  print(str(ansSnake[i][0]+1) +" "+str(ansSnake[i][1]+1))
  
  
  