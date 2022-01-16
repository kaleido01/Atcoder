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


n, k = mapInt()
r, s, p = mapInt()
t = input()

# # 0ぐー、１ちょき、２ぱー
# dp = [ [ [ 0 for _ in range(3)]for _ in range(3)]for _ in range(n+1)]



# for i in range(n+1):
#   for j in range(3):
#     for l in range(3):
#       if t[i] == "r" and j == 2:
#         dp[i+1][j][l] = dp[i][2][]
#       elif t[i] == "s":
#         else t[i] == "r":
        
# print(max(dp))
  
def getScore(ss):
  if ss == "r":
    return p
  elif ss == "s":
    return r
  else:
    return s

ans = 0
for i in range(k):
  isOut = False
  for j in range(i, n, k):
    # print(t[j], getScore(t[j]))
    if j-k < 0:
      ans += getScore(t[j])
      isOut = True
    else:
      if t[j-k] == t[j] and isOut:
        isOut = False
        continue
      ans += getScore(t[j])
      isOut = True
      
print(ans)
    