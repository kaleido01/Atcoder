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


n, q = mapInt()

a = listInt()

def isOk(index, key):
  """不等号を入れ替える場合は呼び出し側のOKとNGのmiddleも入れ替える"""
  # return a[index] <= key
  return a[index] >= key


def binary_search(v):
    # ok = -1
    # ng = len(a)
    ng = -1
    ok = len(a)
    while(abs(ok-ng) > 1):
      middle = (ok + ng) // 2
      if isOk(middle, v):
        ok = middle
      else:
        ng = middle
    return ok

for i in range(q):
  k = int(input())
  ok = binary_search(k)
  if ok == -1:
    print(k)
  elif ok == len(a):
    print(k + len(a))
  else:
    if a[ok] == k:
      print(k+ ok+1)
    else:
      print(k+ ok-1)
  