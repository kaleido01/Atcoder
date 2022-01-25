# -*- coding: utf-8 -*-
from pdb import line_prefix
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
from typing import Deque
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7 # 998244353
d4 = [(1,0),(0,1),(-1,0),(0,-1)]
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


h, w, m = mapInt()
dic = {}
linew = [0] * h
lineh = [0] * w

for i in range(m):
  hi, wi = mapInt()
  hi -= 1
  wi -= 1
  linew[hi] += 1
  lineh[wi] += 1
  dic[(hi, wi)] = True


maxh = max(lineh)   
maxw = max(linew)

wx = []
hy = []

for i in range(w):
  if maxh == lineh[i]:
    wx.append(i)
   
for i in range(h):
  if maxw == linew[i]:
    hy.append(i)
   

ans = maxh + maxw
# print(hy, wx)

for i in hy:
  for j in wx:
    if (i,j) in dic: continue
    print(ans)
    sys.exit()
    
print(ans-1)
      