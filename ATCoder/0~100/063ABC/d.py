# -*- coding: utf-8 -*-
from re import L
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
initAny = lambda n, a: [a for _ in range(n)]


inithwv = lambda h, w, v: [[v for _ in range(w)] for _ in range(h)]
inithw = lambda h: [ list(input()) for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]
bit = lambda n, k:((n >> k) & 1) # nのkビット目
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
# YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

N, A, B = mapInt()

h = []
for i in range(N):
  h.append(int(input()))
  


def isOk(key):
  # keyの回数で全ての敵を撲滅できるか
  sumA = 0
  for i in range(N):
    hp = h[i]
    
    a = binary(key, hp)
    # print(a)
    sumA += a
  # print(key, sumA)
  return sumA <= key
  


def is_ok2(limit, maxLimit, hp):
  # print(limit, maxLimit)
  return A* limit + (maxLimit -limit) * B >= hp

def binary(maxLimit, hp):
    ng = -1
    ok = maxLimit
    while(abs(ok-ng) > 1):
      middle = (ok + ng) // 2
      if is_ok2(middle, maxLimit, hp):
        ok = middle
      else:
        ng = middle
    return ok

def binary_search():
    ng = 0
    ok = 10**9
    while(abs(ok-ng) > 1):
      middle = (ok + ng) // 2
      if isOk(middle):
        ok = middle
      else:
        ng = middle
    return ok
  
  
ans = binary_search()

print(ans)