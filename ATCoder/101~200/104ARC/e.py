# -*- coding: utf-8 -*-
from curses.ascii import islower
from re import L
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
s = input()
n = len(s)
mk = int(input())


# isLower 1: True(すでに下回っている) 0:exactまだ一致している
dp = [ [ [0 for _ in range(5)] for _ in range(2)] for _ in range(n+1)] 
dp[0][0][0] = 1

for i in range(1, n+1):
  for isLower in range(2):
    for k in range(4):
      if isLower:
        dp[i][isLower][k] += dp[i-1][isLower][k] #0を使った場合kは増えない
        dp[i][isLower][k+1] += (9) * dp[i-1][isLower][k] #1-9を使うとkが増える
      else: #この桁まで一致している場合
        cur = int(s[i-1])
        for p in range(cur+1):
          # 0配置はkは増えない
          if p == 0:
            if cur == 0:
              dp[i][0][k] += dp[i-1][0][k]
            else:
              dp[i][1][k] += dp[i-1][0][k]
            continue
          # それ以外はk増加
          if p == cur:
            dp[i][0][k+1] += dp[i-1][0][k]
          else:
            dp[i][1][k+1] += dp[i-1][0][k]
                
                
print(dp[n][0][mk] + dp[n][1][mk])