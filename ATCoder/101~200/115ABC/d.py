# -*- coding: utf-8 -*-
import sys, getpass, string
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
INF=10**18
MOD=10**9+7 # 998244353
sys.setrecursionlimit(10**9)

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

# n = int(input())
# s = input()
# h, w = mapInt()
n, m = mapInt()


a = [0] * (n+1)
b = [0] * (n+1)

# all
a[0] = 1
# p
b[0] = 1

for i in range(1, n+1):
  a[i] = 2*a[i-1] + 3
  b[i] = 2*b[i-1] + 1
  

def count(m,n):
  center = a[n] // 2 + 1
  if n == 0 and m==1:
    return 1
  # print(center, n, m)
  if m == 1:
    return 0
  if 1 < m < center:
    return count(m-1, n-1)
  if m == center:
    return b[n-1] + 1
  if center < m < a[n] :
    return b[n-1] + 1 + count(m-center, n-1)
  if m == a[n]:
    return b[n]
  
  
# print(a, b)
print(count(m, n))