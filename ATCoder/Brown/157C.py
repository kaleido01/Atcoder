# -*- coding: utf-8 -*-
from re import L
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
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

n, m = mapInt()

s =[]

for i in range(m):
  s.append(listInt())
  

# n = 1 -> 0 ~ 9
# n = 2 -> 10 ~ 100
# n = 3 -> 100 ~ 1000
start = 0
if n==2 or n==3:
  start = 10**(n-1)
for i in range(start, 10**n):
  ok = True
  for j in range(m):
    keta = s[j][0]
    v = s[j][1]
    t = str(i)
    if n == 1 and (keta == 2 or keta == 3): 
      ok = False
      break
    if n == 2 and (keta == 3): 
      ok = False
      break
    # print(keta, str(v))
    if t[keta-1] != str(v): 
      ok = False
      break
  if ok:
    print(i)
    sys.exit()

print(-1)
  