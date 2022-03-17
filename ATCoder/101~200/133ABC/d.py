# -*- coding: utf-8 -*-
from genericpath import isfile
from os import getloadavg
from re import L
import sys, getpass, string
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
from types import TracebackType
sys.setrecursionlimit(3*10**5+10)
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

n = int(input())
a = listInt()

def isOver(start):
  if start > a[0]: return True
  
  l = [0] * n
  p = [0] * n
  l[0] = start
  l[-1] = start
  p[0] = 2 * start
  for i in range(1, n):
    x = a[i-1] - l[i-1]
    # print(x)
    if x < 0: return True
    l[i] += x
    l[i-1] += x
    p[i] = 2 * x
  if l[-1] == a[-1]:
    print(*p)
    exit()
  # print(l)
  return l[-1] > a[-1]
  
def binary_search():
    left = -1
    right = 10 ** 10 + 1

    while(right-left > 1):
      middle = (right + left) // 2
      if isOver(middle):
        right = middle
      else:
        left = middle
    return left
  
  
binary_search()
