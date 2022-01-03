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

n = intInput()

# n, m = mapInt()

node = initDp(n)
for i in range(n-1):
  a, b = mapInt()
  a, b = a-1, b-1
  node[a].append(b)
  node[b].append(a)
  

dp = [0] * n
def dfs(pos, pre):
  #自分自身の点を共有するので最低１つは存在
  dp[pos] = 1
  
  for nv in node[pos]:
    if nv != pre:
      #自分より下の部分木についてdpを計算してから足し合わせる。ただし、逆流しないように直前と同じ場所の場合はスキップ
      dfs(nv, pos)
      dp[pos] += dp[nv]

dfs(0, -1)

# print(dp)

ans = 0
for v in dp:
  ans += v * (n-v)
  
print(ans)