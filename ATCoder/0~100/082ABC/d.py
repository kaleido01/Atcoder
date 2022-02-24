# -*- coding: utf-8 -*-
from http.client import OK
from pickle import TRUE
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
from typing import Deque
INF=10**18
MOD=10**9+7 # 998244353
d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
input=lambda: sys.stdin.readline().rstrip()
mapInt = lambda: map(int, input().split())
listInt = lambda: list(map(int, input().split()))

init0 = lambda n: [0 for _ in range(n)]
init1 = lambda n: [-1 for _ in range(n)]
initAny = lambda n, a: [a for _ in range(n)]


inithwv = lambda h, w, v: [[v for _ in range(w)] for _ in range(h)]
inithw = lambda h: [ list(input()) for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]
bit = lambda n, k:((n >> k) & 1) # nのkビット目
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
# YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

# h, w = mapInt()
s = input()
u, v = mapInt()

# m = 16010
# u += m//2
# v += m//2

      

# doneX = [ False for _ in range(m)]
# doneY = [ False for _ in range(m)]

sx = []
sy = []
l = 0
d = 1
while(l < len(s)):
  cnt = 0
  while(l < len(s) and s[l] == "F"):
    l +=1
    cnt +=1
  
  if d: sx.append(cnt)
  else: sy.append(cnt)
  d = not d
  l +=1



# dpX = [[False for i in range(m)]for i in range(len(sx)+1)]
# dpY = [[False for i in range(m)]for i in range(len(sy)+1)]
# dpX = {}


#初回移動のみ右方向のみ
# dpX[1][m//2+sx[0]] = True
# dpX[0][m//2] = True

dpX = {sx[0]: True}
# for i in range(1, len(sx)):
#   for j in range(m):
#     d = sx[i]
#     if j-d >= 0 and dpX[i][j-d]:
#       dpX[i+1][j] = True
#     if j+d < m and dpX[i][j+d]:
#       dpX[i+1][j] = True

for i in range(1, len(sx)):
  temp = {}
  d = sx[i]
  for p in dpX.keys():
    temp[p+d] = True
    temp[p-d] = True
  dpX = temp

dpY = {0: True}
for i in range(len(sy)):
  temp = {}
  d = sy[i]
  for p in dpY.keys():
    temp[p+d] = True
    temp[p-d] = True
  dpY = temp

# print(sx, sy)
# print(dpX, dpY)
# print(dpX, dpY)
# print(v,dpY)
YesNo(u in dpX and v in dpY)