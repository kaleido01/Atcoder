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
# s = input()
# h, w = mapInt()
# n, k = mapInt()

# a = listInt()



def solve(a, s):
  can = True
  # 前の桁が繰り上がりしてるか
  now = 0
  for j in range(60):
    #そのビットを立てる時
    if (a >> j) & 1:
      if (s >> j) & 1:
        if now == 0:
          can = False
          break
      else:
        if now == 1:
          can = False
        now = 1
    #そのビットを立てない(繰り上がりがあってはだめ)
    else:
      if (s >> j) & 1:
        if now == 1:
          now = 0
        else:
          now = 0
  YesNo(not now and can)
          
      
        
        
        

for i in range(n):
  a, s = mapInt()
  solve(a, s)
  

