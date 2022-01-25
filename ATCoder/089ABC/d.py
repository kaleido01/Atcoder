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
inithw = lambda h: [ list(map(int, input().split())) for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]
bit = lambda n, k:((n >> k) & 1) # nのkビット目
# YesNo=lambda b: bool([print('Yes')] if b else print('No'))
# YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

h, w, d = mapInt()


a = inithw(h)
dic = [(0, 0)] * (h*w+1)
for i in range(h):
  for j in range(w):
    x = a[i][j]
    dic[x] = (i, j)

# md = h*w + 1 // d
# s = [ [ 0 for i in range(h * w + 1)] for i in range(d)]
s = [  0 for _ in range(h * w + 1)]

for i in range(d):
  for j in range(i, h*w+1 - d, d):
    yc, xc = dic[j]
    yn, xn = dic[j+d]
    s[j+d] = s[j] + abs(yn-yc) + abs(xn-xc)
    

q = int(input())

for i in range(q):
  l, r = mapInt()
  init = l % d
  ans = s[r] - s[l]
  print(ans)
