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
# YesNo=lambda b: bool([print('Yes')] if b else print('No'))
# YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1


a, b, c, d = mapInt()

x = [a, b, c, d]
# if a == b+c+d:
#   print("Yes")
# elif b == a+c+d:
#   print("Yes")
# elif c == b+a+d:
#   print("Yes")
# elif d == b+c+a:
#   print("Yes")
# elif a+b == c+d:
#   print("Yes")
# elif a+c == b+d:
#   print("Yes")
# elif a+d == b+c:
#   print("Yes")
  
s = a + b + c+ d

for i in range(4):
  if x[i] == s - x[i]:
    print("Yes")
    sys.exit()
for i in range(3):
  for j in range(i+1, 4):
    if x[i] + x[j] == s - x[i]-x[j]:
      print("Yes")
      sys.exit()
      
print("No")