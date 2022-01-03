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

n, p, q = mapInt()

a = listInt()

pattern = itertools.combinations(a, 5)

count = 0
for v in pattern:
  x, y, z ,w, r = v
  last = (x * y) %p
  last = (last * z) %p
  last = (last * w) %p
  last = (last * r) %p
  if last == q:
    count += 1
    
    
    
# for i in range(n-4):
#   for j in range(i+1, n-3):
#     for k in range(j+1, n-2):
#       for l in range(k+1, n-1):
#         for m in range(l+1, n):
#           x = 1
#           x == a[i] %p
#           x *= a[j] %p
#           x *= a[k] %p
#           x *= a[l] %p
#           x *= a[m] %p
#           x %= p
#           if x == q:
#             count +=1

print(count)
