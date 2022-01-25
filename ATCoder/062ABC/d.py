# -*- coding: utf-8 -*-
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect, statistics
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
inithw = lambda h: [ list(map(int, input().split())) for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]
bit = lambda n, k:((n >> k) & 1) # nのkビット目
# YesNo=lambda b: bool([print('Yes')] if b else print('No'))
# YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

n = int(input())

a = listInt()

ls = [0] * (n+1)
rs = [0] * (n+1)
lsum = 0
rsum = 0 
leftHeap = []
rightHeap = []

for i in range(n):
  lsum += a[i]
  # rsum += a[-1*(i+1)]
  rsum += a[3*n-i-1]
  
  heapq.heappush(leftHeap, a[i])
  heapq.heappush(rightHeap, -1 * a[3*n-i-1])
  

ls[0] = lsum
rs[0] = rsum
# print(ls, rs)
for i in range(n, 2*n):
  mi = heapq.heappop(leftHeap)
  # 一番小さいものを見て、それより大きい場合は更新
  if mi < a[i]:
    lsum -= mi
    lsum += a[i]
    ls[i - n + 1] = lsum
    heapq.heappush(leftHeap, a[i])
  else:
    ls[i- n + 1] = lsum
    heapq.heappush(leftHeap, mi)
    
    
for i in range(n, 2*n):
  ma = heapq.heappop(rightHeap)
  ma *= -1
  if ma > a[3*n-i-1]:
    rsum -= ma
    rsum += a[3*n-i-1]
    rs[i - n + 1] = rsum
    heapq.heappush(rightHeap, -1 * a[3*n-i-1])
  else:
    rs[i - n + 1] = rsum
    heapq.heappush(rightHeap, -1 * ma)

rs.reverse()
ans = - (1 << 60)
for i in range(n+1):
  ans = max(ans, ls[i] - rs[i])
# print(ls, rs)
print(ans)
  