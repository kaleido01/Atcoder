# -*- coding: utf-8 -*-
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
from typing import Awaitable
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7 # 998244353
d4 = [(0,1), (1,0)]
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

h, w, just = mapInt()

grid = [ list(input()) for _ in range(h)]

def temp():
  temp = [ [ "." for _ in range(w)] for _ in range(h)]
  for i in range(h):
    for j in range(w):
      temp[i][j] = grid[i][j]
      
  return temp

def check(arr):
  cnt = 0
  for i in range(h):
    for j in range(w):
      if arr[i][j] == "#": cnt += 1
      
  return cnt == just
  

ans = 0
for i in range(2 ** h):
  for j in range(2 ** w):
    t = temp()
    # print(t)
    for k in range(h):
      #横1行が赤になる.
      if (i >> k) & 1:
        for x in range(w):
          t[k][x] = "R"
    for l in range(w):
      #縦1行が赤になる. 
      if (j >> l) & 1:
        for y in range(h):
          t[y][l] = "R"
    if check(t): ans +=1
    
print(ans)
  
          