# -*- coding: utf-8 -*-
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
mapInt = lambda: map(int, input().split())
listInt = lambda: list(map(int, input().split()))

init0 = lambda n: [0 for _ in range(n)]
inithwv = lambda h, w, v: [[v for _ in range(w)] for _ in range(h)]
inithw = lambda h, w: [ listInt() for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]

YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1
from operator import itemgetter

n, m = mapInt()

a = [False] * (n+1)
for i in range(m):
  a[int(input())] = True
  

dp = [0] *(n+1)

dp[0] = 1

for i in range(1, n+1):
  # 1dan
  if a[i]: continue
  if i-1 >= 0:
    dp[i] += dp[i-1]
  #dan
  if i-2 >= 0:
    dp[i] += dp[i-2]
  dp[i] %= MOD
  
# print(dp)
print(dp[n])

  
