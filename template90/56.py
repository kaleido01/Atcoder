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
intInput = lambda: int(input())
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

n, s = mapInt()

l = []
for i in range(n):
  l.append(listInt())
  
dp = [ [ "Impossible" for _ in range(s+1)] for _ in range(n+1)]
dp[0][0] = ""

for i in range(1, n+1):
  for j in range(0, s+1):
    a, b = l[i-1]
    if  0 <= j-a <= s:
      if dp[i-1][j-a] != "Impossible":
        dp[i][j] = dp[i-1][j-a] + "A"
      
    if  0 <= j-b <= s:
      if dp[i-1][j-b] != "Impossible":
        dp[i][j] = dp[i-1][j-b] + "B"
      
      
# print(dp)
print(dp[n][s])
