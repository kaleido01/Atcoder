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


n = int(input())


# 0 = A , 1 = G, 2 = C, 3 = T
# forbidden 
# 012,
# 102,
# 021
dp = [ [ [ [ 0 for i in range(4)] for i in range(4)] for i in range(4)]for i in range(n+1)]
def ok(x,y,z, ne):
    return not ((x == 0 and y == 1 and ne == 2) or (x == 0 and z == 1 and ne == 2))

def okW(x, y, z):
    return not ((x == 0 and y == 1 and z == 2) or (x == 1 and y == 0 and z == 2) or (x == 0 and y == 2 and z == 1))

for i in range(4):
    for j in range(4):
        for k in range(4):
            if okW(i, j, k):
                dp[3][i][j][k] = 1



for i in range(2, n):
    for s1 in range(4):
        for s2 in range(4):
          for s3 in range(4):
            for ne in range(4):
                if ok(s1, s2, s3, ne) and okW(s2,s3,ne):
                    dp[i+1][s2][s3][ne] += dp[i][s1][s2][s3]
                    dp[i+1][s2][s3][ne] %= MOD
                # else:
                #     dp[i+1][s2][ne] = 0
ans = 0

for i in range(4):
    for j in range(4):
      for k in range(4):
        ans += dp[n][i][j][k]
        ans %= MOD
# print(dp)
print(ans)