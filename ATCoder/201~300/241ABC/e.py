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

# n = int(input())
# s = input()
n, k = mapInt()
a = listInt()

cnt = {}
ar = []
now = 0
while(now % n not in cnt):
  # now %= n
  cnt[now % n] = True
  ar.append(now % n)
  now += a[now % n]
  

roopStart = now % n
p = 0

for i in range(len(ar)):
  if roopStart == ar[i]:
    p = i
    break
  

s1 = [0] * (p+1)
s2 = [0] * (len(ar) - p + 1)

for i in range(p):
  s1[i+1] = s1[i] + a[ar[i]]

new = ar[p:]
for i in range(len(ar) - p):
  s2[i+1] = s2[i] + a[new[i]]


# print(roopStart, p, ar, new)
# print(s1, s2, len(ar) -p)
if k - p > 0:
  times = (k-p) // (len(ar) - p)
  k = (k-p) % (len(ar) - p)
  
  before = new[k-1]
  ans = s1[p] + times*s2[len(ar) - p] + s2[k]
  print(ans)
else:
  ans = s1[k]
  print(ans)
  
