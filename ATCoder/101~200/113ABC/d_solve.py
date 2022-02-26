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
    exit()

dp = [ [ 0 for i in range(w)] for i in range(h+1)]
dp[0][0] = 1


def check(mask):
    for i in range(w-2):
        a = (mask >> i) & 1
        b = (mask >> (i+1)) & 1
        if a & b: return False
    return True

for i in range(h):
    for j in range(w):
        for mask in range(2 ** (w-1)):
            if not check(mask): continue
            if (mask & (1 << j)):
                dp[i+1][j+1] += dp[i][j]
                dp[i+1][j+1] %= MOD
            elif 0 < j and (mask & (1 << (j-1))):
                dp[i+1][j-1] += dp[i][j]
                dp[i+1][j-1] %= MOD
            else:
                dp[i+1][j] += dp[i][j]
                dp[i+1][j] %= MOD

# print(dp)
print(dp[h][K-1])