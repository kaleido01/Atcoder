# -*- coding: utf-8 -*-
from ast import Mod
from operator import mod, truediv
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


h, w, K = mapInt()

if w==1:
    print(1)

dp = [ [ 0 for i in range(w+1)] for i in range(h+1)]
dp[0][1] = 1


def check(x):


for i in range(h):
    for j in range(1, w+1):
        #遷移しない
        if j == 1 or j == w:
            dp[i+1][j] += dp[i][j] * 2**(f(w-2))
        else:
            dp[i+1][j] += dp[i][j] * 2**(f(w-3))
        dp[i+1][j] %= MOD
        
        
        # 右側にしか遷移できない
        if j == 1:
            dp[i+1][j+1] += dp[i][j] * 2**(f(w-3))
        #　 左側のみ
        elif j == w:
            dp[i+1][j-1] += dp[i][j] * 2**(f(w-3))
        else:
            if j+1 == w:
                dp[i+1][j+1] += dp[i][j] * 2**(f(w-3))
            else:
                dp[i+1][j+1] += dp[i][j] * (2 ** (w-4))
            if j-1 == 1:
                dp[i+1][j-1] += dp[i][j] * 2**(f(w-3))
            else:
                dp[i+1][j-1] += dp[i][j] * (2 ** (w-4))
        if j-1>=1:
            dp[i+1][j-1] %= MOD
        if j+1<=w:
            dp[i+1][j+1] %= MOD

print(dp)
print(dp[h][K])