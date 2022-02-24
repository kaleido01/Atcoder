# -*- coding: utf-8 -*-
import sys, getpass, string
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

a, b, c = mapInt()


dic = {
  0: [0],
  1: [1],
  2: [2,4,8,6],
  3: [3,9,7,1],
  4: [4,6],
  5: [5],
  6: [6],
  7: [7,9,3,1],
  8: [8,4,2,6],
  9: [9,1]
}
if a%10 == 0:
  print(0)
  exit()



b1 = b % 10
if b1 == 0:
  a1 = a % 10
  z = len(dic[a1])
  b1 = (b-1) % z

x = len(dic[b1])
c = (c-1)%x

y = dic[b1][c]

# print(y)
a1 = a % 10
z = len(dic[a1])
a = (y-1) % z

print(dic[a1][a])


