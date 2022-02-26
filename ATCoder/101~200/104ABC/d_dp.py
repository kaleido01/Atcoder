# -*- coding: utf-8 -*-
import sys, getpass, string
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
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
# YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1
MOD=10**9+7 # 998244353

s = input()
n = len(s)

dp = [ [0 for i in range(4)] for i in range(n+1)]

dp[0][0] = 1

for i in range(n):
  for state in range(4):
    
    #状態変化なし. ?は任意で変化できるので今ある状態が三倍になる
    # それ以外は、同じ個数がそのまま遷移
    if s[i] == "?":
      dp[i+1][state] += 3*dp[i][state]
    else:
      dp[i+1][state] += dp[i][state]

    # 状態遷移あり、該当stateからその次のstateへ行くためには、
    # みている文字が該当stateの次の文字、もしくは任意で選べる？であることが必要条件
    if state == 0:
      if s[i] == "A" or s[i] == "?":
        dp[i+1][state+1] = dp[i][state]
    if state == 1:
      if s[i] == "B" or s[i] == "?":
        dp[i+1][state+1] = dp[i][state]
    if state == 2:
      if s[i] == "C" or s[i] == "?":
        dp[i+1][state+1] = dp[i][state]
    dp[i+1][state] %= MOD
    if state < 3:
      dp[i+1][state+1] %= MOD
    
print(dp[n][3])
