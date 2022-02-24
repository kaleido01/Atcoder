# -*- coding: utf-8 -*-
from posixpath import split
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

# h, w = mapInt()
n = list(map(int, list(input())))
# print(n)

for i in range(2):
  for j in range(2):
    for k in range(2):
      ans = 0
      op1 = ""
      op2 = ""
      op3 = ""
      if i:
        ans+= n[0] + n[1]
        op1 = "+"
      else:
        ans+= n[0] - n[1]
        op1 = "-"
      if j:
        ans+= n[2]
        op2 = "+"
      else:
        ans-= n[2]
        op2 = "-"
      if k:
        ans+= n[3]
        op3 = "+"
      else:
        ans-= n[3]
        op3 = "-"
      if ans == 7:
        print(str(n[0])+op1+str(n[1])+op2+str(n[2])+op3+str(n[3])+"=7")
        exit()
