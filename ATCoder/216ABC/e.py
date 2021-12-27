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
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

n, k = mapInt()

v = listInt()
v.append(0)
# 1111   6666        8888888
v.sort()
v = v[::-1]
a = init0(n)
s = init0(n+1)
x = init0(n+1)
p = init0(n+1)
currentNewVCount= 1
# print(v)

def sum(n):
  return n*(n+1)//2
    
currentAns = 0

currentV = v[0]
for i in range(1, n+1):
  if currentV == v[i]:
    currentNewVCount += 1
    x[i] = x[i-1]
    p[i] = p[i-1]
    s[i] = s[i-1]
  else:
    x[i] = x[i-1] + currentNewVCount
    p[i] = p[i-1] + x[i] * (currentV - v[i])

    if k <= p[i]:
      r = (k - p[i-1]) // x[i]
      m = (k - p[i-1]) % x[i]
      currentAns = s[i-1] + x[i] * (sum(currentV) - sum(currentV - r)) + (currentV- r) * m
      print(currentAns)
      sys.exit()

    s[i] = s[i-1] + x[i] * (sum(currentV) - sum(v[i]))
    currentV = v[i]
    currentNewVCount = 1
    

# print(a,s,x,p)
print(s[-1])
# print(currentAns, s, x, p)
