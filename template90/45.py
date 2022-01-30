# 巡回セールス問題(全頂点一度のみ, 戻らなくて良い)

# -*- coding: utf-8 -*-
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
from unicodedata import name
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

n, k = mapInt()
pointer = []
for i in range(n):
  pointer.append(listInt())

# DPテーブルは−１で初期化。−１でないところはすでに探索済みを表す
dp = [[-1 for _ in range(n)] for _  in range(1 << n)]



#集合と終点を管理
def rec(bit, cv):
  if dp[bit][cv] != -1: return dp[bit][cv]
  
  #初期値 ( 100000 )
  if bit == (1 << cv):
    dp[bit][cv] = 0
    return dp[bit][cv]

  # 答え
  res = INF
  
  # bitのvを除いたもの( ~ は反転を意味する->v地点だけ1にして反転-> 論理積を取ることで、vの場所だけ落としたものが取れる)
  prev_bit = bit & (~(1<<cv))
  
  # vの手前のノードとしてuを全探索
  for u in range(n):
    if not (prev_bit & (1 << u)): continue #uがprev_bitになかったらダメ
    if dist[u][cv] == -1: continue
    
    #再起的に探索
    if res > (rec(prev_bit, u) + dist[u][cv]):
      res = rec(prev_bit, u) + dist[u][cv]
    
    
  dp[bit][cv] = res
  return dp[bit][cv]

ans = INF
for i in range(n):
  if ans > rec((1<<n)-1, i):
    ans = rec((1<<n)-1, i)
    
# print(dp)
print(ans)