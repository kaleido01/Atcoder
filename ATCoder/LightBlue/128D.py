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

v = listInt()
m = 0

ans = -INF
for i in range(min(k+1, n+1)):
  rest = k - i
  for j in range(i+1):
    left = i-j
    right = j
    
    minheap = []
    done = [False] * n
    s = 0
    for p in range(0, left):
      done[p] = True
      s += v[p]
      if v[p] < 0:
        heapq.heappush(minheap, v[p])
    
    for p in range(n-1,max(-1, n-1-right), -1):
      if done[p]: break
      # print("p", p)
      s += v[p]
      if v[p] < 0:
        heapq.heappush(minheap, v[p])

    # print("left, right", left, right)
    # print(rest, minheap, s)
    temp = rest
    while temp and minheap:
      pop = heapq.heappop(minheap)
      if pop < 0:
        s -= pop
        temp -= 1
      else:
        break 
    ans = max(ans, s)
print(ans)