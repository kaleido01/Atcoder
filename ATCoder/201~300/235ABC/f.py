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

n, s = mapInt()

mod = 998244353
a = listInt()

dp = [[0 for i in range(s+1)]  for i in range(n+1)]
dp[0][0] = 1
ans = 0
for i in range(n):
  dp[i+1][0] += 1
  for j in range(s+1):
    if j-a[i] >= 0:
      dp[i+1][j] += (dp[i][j-a[i]] + dp[i][j]) % mod
    else:
      dp[i+1][j] += dp[i][j] % mod
  ans += dp[i+1][s]
  ans %= mod
      
# print(dp)
print(ans % mod)