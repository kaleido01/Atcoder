# -*- coding: utf-8 -*-
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect, statistics
from collections import Counter, defaultdict, deque
from typing import ItemsView
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

n , k = mapInt()

a = listInt()

bin_str = format(k, 'b')

rest = 50 - len(bin_str)
u = "0" * rest + bin_str
# k = bin_str
l = len(u)

# この戦略の場合うまくいかない(ACになるけど...)
# dp = [ False for _ in range(l+1)]

# # falseになったタイミングで任意の 1,0を選択できる
# ans = 0
# for i in range(l):
#   cnt1 = 0
#   cnt0 = 0
#   for j in range(n):
#     # print(a[j], keta-i-1)
#     if (a[j] >> (l - i - 1)) & 1:
#       cnt1 += 1
#     else:
#       cnt0 += 1
#   #何でも良い
#   # print(cnt1, cnt0)
#   if dp[i]:
#     if cnt0 >= cnt1:
#       ans += cnt0 * 2**(l-i-1)
#     else:
#       ans += cnt1 * 2**(l-i-1)
#     dp[i+1] = True
#   #直前まで一致している場合、次の桁が1 or 0かで変わる
#   else:
#     if (int(k) >> l - i - 1) & 1:
#       if cnt0 > cnt1:
#         ans += cnt0 * 2 ** (l-i-1)
#       else: #次回以降なんでも良い
#         ans += cnt1 * 2**(l-i-1)
#         dp[i+1] = True
#     else: #0以外選択できない
#         ans += cnt1 * 2 ** (l-i-1)
#   # print(ans)
# print(ans)
    
    
# 0 or 1 0は桁が一致, 1はANY
# dp[i][j] i桁目まで見た時に、得られる最大値、j = 0 は直前まで一致している時
dp = [[-1, -1] for _ in range(l+1)]
dp[0][0] = 0
for i in range(l):
  cnt1 = 0
  for j in range(n):
    if (a[j] >> (l - i - 1)) & 1:
      cnt1 += 1
  # print(cnt1, cnt0)
  #直前がまだ一致している時
  #その桁が１なら好きな方をとれる
  # print(int(k), int(k) >> l - i - 1)
  # if (int(k) >> l - i - 1) & 1:
  #     dp[i+1][0] = dp[i][0] + cnt0 * 2 ** (l-i-1)
  #     # 1を取れるのに0を選択する場合は次回以降はAny
  #     dp[i+1][1] = max(dp[i][0], dp[i][1]) + cnt1 * 2 ** (l-i-1)
  # else: #0以外選択できない
  #     dp[i+1][0] = dp[i][0] + cnt1 * 2 ** (l-i-1)
  #     # すでに下はなんでも良い
  #     if dp[i][1] == 0:
  #       continue
  #     else:
  #       dp[i+1][1] = max(dp[i][1], dp[i][0]) + max(cnt0, cnt1) * 2 ** (l-i-1)
  
  # ビットが立っている方を加える(Xでのbitは0)
  # print(cnt1)
  # print(k, (k >> l - i - 1) & 1, l-i-1)

  add1 = cnt1 * 2**(l-i-1)
  add0 = (n-cnt1) * 2**(l-i-1)
  # print(add1, add0)
  # smaller -> smaller
  if dp[i][1] != -1:
    dp[i+1][1] = max(dp[i+1][1], dp[i][1] + max(add1, add0))
    
  # exact -> smaller
  if dp[i][0] != -1:
    if (k >> (l - i - 1)) & 1:
      dp[i+1][1] = max(dp[i+1][1], dp[i][0] + add1)
  
  # exact -> exact
  if dp[i][0] != -1:
    if (k >> (l - i - 1)) & 1:
      dp[i+1][0] = max(dp[i+1][0], dp[i][0] + add0)
    else:
      dp[i+1][0] = max(dp[i+1][0], dp[i][0] + add1)
    

  
# print(dp)
print(max(dp[l][0], dp[l][1]))
