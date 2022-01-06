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
inithw = lambda h: [ list(input()) for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]
bit = lambda n, k:((n >> k) & 1) # nのkビット目
# YesNo=lambda b: bool([print('Yes')] if b else print('No'))
# YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1


def isOk1(index, key):
  """不等号を入れ替える場合は呼び出し側のOKとNGのmiddleも入れ替える"""
  return lm[index] >= key
  # return a[index] >= key

def isOk2(index, key):
  """不等号を入れ替える場合は呼び出し側のOKとNGのmiddleも入れ替える"""
  return rm[index] >= key
  # return a[index] >= key


def binary_search1(v, a):
    ok = len(a)
    ng = -1
    # ng = -1
    # ok = len(a)
    while(abs(ok-ng) > 1):
      middle = (ok + ng) // 2
      if isOk1(middle, v):
        ok = middle
      else:
        ng = middle
    return ok
        
def binary_search2(v, a):
    ok = len(a)
    ng = -1
    # ng = -1
    # ok = len(a)
    while(abs(ok-ng) > 1):
      middle = (ok + ng) // 2
      if isOk2(middle, v):
        ok = middle
      else:
        ng = middle
    return ok

n = int(input())
a = listInt()

lm = []
rm = []
x1 = [0] * n
x2 = [0] * n

lm.append(a[0])
x1[0] = 1
for i in range(1, n):
  if a[i] > lm[-1]:
    lm.append(a[i])
  else:
    pos = binary_search1(a[i], lm)
    if pos == len(lm):
        lm.append(a[i])
    else:
      lm[pos] = a[i]
  # print(lm)
  x1[i] = len(lm)

rm.append(a[-1])
x2[0] = 1
for i in range(n-1, -1, -1):
  if a[i] > rm[-1]:
    rm.append(a[i])
    
  else:
    pos = binary_search2(a[i], rm)
    if pos == len(rm):
        rm.append(a[i])

    else:
      rm[pos] = a[i]
  # print(rm)
  x2[i] = len(rm)

      
# print(lm, rm)
# print(x1, x2)
ans = 0
for i in range(n):
  ans = max(ans, x1[i] + x2[i]-1)
print(ans)

