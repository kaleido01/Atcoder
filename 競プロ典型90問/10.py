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
# YesNo=lambda b: bool([print('Yes')] if b else print('No'))
# YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

n = int(input())

c1 = init0(n)
c2 = init0(n)


for i in range(n):
  c, p = mapInt()
  if c == 1:
    c1[i] = p
  else:
    c2[i] = p
  
  
s1 = init0(n + 1)
s2 = init0(n + 1)

for i in range(len(c1)):
  s1[i+1] = s1[i] + c1[i]

for i in range(len(c2)):
  s2[i+1] = s2[i] + c2[i]


q = int(input())

# print(s1, s2)
for i in range(q):
  l, r = mapInt()
  
  x = s1[r] - s1[l-1]
  y = s2[r] - s2[l-1]
  
  print(str(x) + " " + str(y))
  
  