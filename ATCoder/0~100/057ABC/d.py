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

n, u, v = mapInt()
a = listInt()

a.sort(reverse=True)

cntAll = {}
for i in range(n):
  if a[i] in cntAll:
    cntAll[a[i]] += 1
  else:
    cntAll[a[i]] = 1
cnt = {}
ansA = 0
ansB = 1
temp= 0
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
for i in range(n):
  if i >= v: break
  temp += a[i]
  
  if a[i] in cnt:
    cnt[a[i]] += 1
  else:
    cnt[a[i]] = 1
  if i == u-1:
    ansA = temp / u
    for k, v1 in cnt.items():
      v2 = cntAll[k]
      ansB *= combinations_count(v2, v1)
  elif i >= u and temp / (i+1) == ansA:
    t = 1
    for k, v1 in cnt.items():
      v2 = cntAll[k]
      t *= combinations_count(v2, v1)
    ansB += t
  elif i < u:
    continue
  else:
    break
  


print(ansA)
print(ansB)