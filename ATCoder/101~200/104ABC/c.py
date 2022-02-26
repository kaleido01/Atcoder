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

# n = int(input())
# s = input()
d, g = mapInt()

problems = []
for i in range(d):
  problems.append(listInt())

dp = {}
dp = {0: 0}
for i in range(d):
  p, c = problems[i]
  temp = {}
  for score, minP in dp.items():
    for solve in range(0, p+1):
      add = (1+i) * 100 * solve
      if solve == p:
        add += c
      
      if score+add in temp:
          temp[score + add] = min(temp[score + add], minP + solve)
      else:
        # if score+add in dp:
        #   temp[score + add] = min(dp[score+add], minP + solve)
        # else:
          temp[score + add] = minP + solve
  dp = temp
# print(dp)

ans = INF
for k,v in dp.items():
  if k >= g:
    ans = min(v, ans)
print(ans)


