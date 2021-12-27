# -*- coding: utf-8 -*-
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7 # 998244353
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
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


h , w = mapInt()

grid = inithw(h)

ans = 0

left = [0, 0]
right = [0, 0]
start = False
for i in range(1, h):
  count = 0
  for j in range(1, w):
    p = -1
    q = -1
    if grid[i][j] == "#":
      if count == 0:
        p = j
        count += 1
      else:
        q = j
        count = 2
  # print("count", count)
  if count == 1:
    if not(p == left[0] and left[0] == left[1]):
      ans += 1
      left[0], left[1] = p, left[0]
    if not(p == right[0] and right[0] == right[1]):
      ans += 1
      right[0], right[1] = p, right[0]
  if count == 2:
    if not(p == left[0] and left[0] == left[1]):
      ans += 1
      left[0], left[1] = p, left[0]
    if not(q == right[0] and right[0] == right[1]):
      ans += 1
      right[0], right[1] = q, right[0]
  
  # print(ans)
  if start:
    continue
  if not start and count == 1:
    ans = 1
    start = True
  if not start and count == 2:
    ans = 2
    start = True
  

if ans <=2:
  print(4)
else:
  print(ans)