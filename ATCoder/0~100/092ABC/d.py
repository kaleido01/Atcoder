# -*- coding: utf-8 -*-
from audioop import reverse
from re import X
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
bit = lambda n, k:((n >> k) & 1) # nのkビット目
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1
from operator import itemgetter
from collections import deque
import heapq




a, b = mapInt()

grid = []

for i in range(100):
  if i < 50:
    grid.append(["#"] * 100)
  else:
    grid.append(["."] * 100)
    
    
    
cnt = 0
for i in range(0, 100, 2):
  for j in range(0, 100, 2):
    if cnt < a-1:
      grid[i][j] = "."
      cnt +=1
    else:
      break
  
  if cnt >= a-1:
    break
  
cnt = 0
for i in range(51, 100, 2):
  for j in range(0, 100, 2):
    if cnt < b-1:
      grid[i][j] = "#"
      cnt +=1
    else:
      break
  
  if cnt >= b-1:
    break
  
print(100, 100)
for i in range(100):
  print("".join(grid[i]))


