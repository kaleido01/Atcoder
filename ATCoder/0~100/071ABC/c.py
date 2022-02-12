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


x = int(input())
a = listInt()

cnt = {}

for i in range(x):
  if a[i] in cnt:
    cnt[a[i]] +=1
  else:
    cnt[a[i]] =1
  
lis1 = []
lis2 = []

for k, v in cnt.items():
  if v >= 4:
    lis1.append(k)
  elif v == 2 or v == 3:
    lis2.append(k)
    

ans = -1
lis1.sort(reverse=True)
lis2.sort(reverse= True)
# print(lis1, lis2)
if len(lis1) > 0:
  ans = lis1[0] ** 2
if len(lis2) >= 1 and len(lis1) > 0:
    ans = max(lis1[0] * lis2[0], ans)
    
if len(lis2) >= 2:
    ans = max(lis2[0] * lis2[1], ans)
    

if ans == -1:
  print(0)
else:
  print(ans)

