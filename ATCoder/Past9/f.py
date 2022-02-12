# -*- coding: utf-8 -*-
from collections import deque
import hmac
from re import L
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


x, y = mapInt()
x -=1
y -=1
hMax = 9
wMax = 9

masu = [list(input()) for i in range(3)]

done = [ [ False for i in range(wMax)] for i in range(hMax)]

q = deque()


q.append((x,y))
done[x][y] = True




while q:
  px, py = q.popleft()
  
  for i in range(3):
    for j in range(3):
      if masu[i][j] == "#":
        nx = px + i+1 - 2
        ny = py + j+1 - 2
        
        if not(0<= nx < wMax and 0 <= ny < hMax): continue
        if done[nx][ny]:continue
        
        done[nx][ny] = True
        q.append((nx, ny))
        
ans = 0
for i in range(hMax):
  for j in range(wMax):
    if done[i][j]: ans +=1
    
print(ans)


  