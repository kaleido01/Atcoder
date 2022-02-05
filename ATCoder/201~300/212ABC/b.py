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
int1=lambda x:int(x)-1

a = input()

x = []
x.append(int(a[0]))
x.append(int(a[1]))
x.append(int(a[2]))
x.append(int(a[3]))


def f1 ():
  return x[1] == x[2] == x[3] == x[0]
  
def f2():
  isOK = True
  cnt = 0
  for i in range(3):
    if (x[i] + 1) % 10 == x[i+1] % 10:
      isOK = False
      cnt += 1
  # print(cnt)
  return cnt == 3

if f1() or f2():
  print("Weak")
else:
  print("Strong")