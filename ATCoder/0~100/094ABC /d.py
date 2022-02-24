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

n, m = mapInt()

a = listInt()
a.sort(reverse=True)
# for i in range(nee)
need = [0,2,5,5,4,5,6,3,7,6]
dp = [ -1 for i in range(n+1)]
dp[0] = 0


# 最大桁
for i in range(n+1):
  for j in range(m):
    if dp[i] != -1:
      cost = need[a[j]]
      # print(cost)
      if i + cost > n: continue
      if dp[i+cost] != -1:
        dp[i+cost] = max(dp[i+cost], dp[i] + 1)
      else:
        # print("aaaa")
        # print(dp[i], dp[i]+1)
        dp[i+cost] = dp[i] + 1
        # print(dp[i+cost])

#桁を復元
ans = []
k = n
# print()
while k > 0:
  for j in range(m):
    d = a[j]
    if k-need[d] >= 0 and dp[k-need[d]] == dp[k] - 1:
      ans.append(str(d))
      k = k-need[d]
      break

      
      
print("".join(ans))