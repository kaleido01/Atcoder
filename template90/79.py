# -*- coding: utf-8 -*-
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect, statistics
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
init1 = lambda n: [-1 for _ in range(n)]

inithwv = lambda h, w, v: [[v for _ in range(w)] for _ in range(h)]
inithw = lambda h: [ list(map(int, input().split())) for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]
bit = lambda n, k:((n >> k) & 1) # nのkビット目
# YesNo=lambda b: bool([print('Yes')] if b else print('No'))
# YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

h, w = mapInt()

a = inithw(h)
b = inithw(h)

diff  = inithwv(h, w, 0)

for i in range(h):
  for j in range(w):
    
    diff[i][j] = int(a[i][j]) - int(b[i][j])

# print(diff)
  

ans = 0
for i in range(h-1):
  for j in range(w-1):
    ans += abs(diff[i][j])
    v = diff[i][j]
    diff[i][j] -= v
    diff[i+1][j] -= v
    diff[i][j+1] -= v
    diff[i+1][j+1] -= v
    
ok = True
# print(diff)
for i in range(h):
  for j in range(w):
    if diff[i][j] != 0:
      print("No")
      sys.exit()

print("Yes")
print(ans)