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

inithwv = lambda h, w, v: [[v for _ in range(w)] for _ in range(h)]
inithw = lambda h: [ list(input()) for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]
bit = lambda n, k:((n >> k) & 1) # nのkビット目
# YesNo=lambda b: bool([print('Yes')] if b else print('No'))
# YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

n = int(input())



p = [ listInt() for _ in range(n)]

  
p.sort(key= lambda x: x[0])


# ソート + ビット全探索
# ans = 0
# for i in range(2**n):
#   end = 1
#   temp = 0
#   ok = True
#   for j in range(n):
#     if (i >> j) & 1:
#       d, c, s = p[j]
#       # print(end)
#       if end + c - 1 >= d:
#         ok = False
#         break
#       end += c
#       temp += s
      
#   if ok:
#     ans = max(ans, temp)

# print(ans)  
  
  
mD = 5010
dp = [ [0 for _ in range(mD)] for _ in range(n+1)]

# DP実装。　i番目のタスクまで、合計j日目の終わりまでに得られる金額の最大値。
# 更新可能な時はi番目のタスクの j-c日目の終わりが0日以上であり、終了日（ここまでの合計)jがd以下であること。
for i in range(1, n+1):
  for j in range(mD):
    d, c, s = p[i-1]
    if j - c >= 0  and j <= d:
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-c] + s)
    else:
      dp[i][j] = dp[i-1][j]

# print(dp)
print(max(dp[n]))