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
init1 = lambda n: [-1 for _ in range(n)]
initAny = lambda n, a: [a for _ in range(n)]


inithwv = lambda h, w, v: [[v for _ in range(w)] for _ in range(h)]
inithw = lambda h: [ list(input()) for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]
bit = lambda n, k:((n >> k) & 1) # nのkビット目
# YesNo=lambda b: bool([print('Yes')] if b else print('No'))
# YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

# h, w = mapInt()
n = input()


dp = [ [ [0] * 2 for i in range(10)] for i in range(len(n)+1)]
# dp = [ [0] * 2 for i in range(len(n)+1)]



for k in range(len(n)):
    for isSmaller in range(2):
      if isSmaller:
        s = 0
        for d in range(10):
          s += dp[k][d][1]
        for d in range(10):
          if s == 0:
            dp[k+1][1][isSmaller] += 1
            dp[k+1][d][isSmaller] += 0
          else:
            dp[k+1][1][isSmaller] += 2*s
            dp[k+1][1][isSmaller] += s
      else:
        p = int(n[k])
        for x in range(p+1):
          if x == p:
            if x == 1:
              dp[k+1][x][0] += dp[k][x][0] + 1
            else:
              dp[k+1][x][0] += dp[k][x][0]
          else:
            if x == 1:
              dp[k+1][x][1] += dp[k][x][0] + 1
            else:
              dp[k+1][x][1] += dp[k][x][0]

# for k in range(len(n)):
#     for isSmaller in range(2):
#       if isSmaller:
#         for d in range(10):
#           if d == 1:
#             dp[k+1][isSmaller] += dp[k][isSmaller] + 1
#           else:
#             dp[k+1][isSmaller] += dp[k][isSmaller]
#       else:
#         p = int(n[k])
#         print(k)
#         for d in range(p+1):
#           if d == p:
#             if d == 1:
#               dp[k+1][0] += dp[k][0] + 1
#             else:
#               dp[k+1][0] += dp[k][0]
#           else:
#             if d == 1:
#               dp[k+1][1] += dp[k][0] + 1
#             else:
#               dp[k+1][1] += dp[k][0]


print(dp)
print(dp[len(n)])