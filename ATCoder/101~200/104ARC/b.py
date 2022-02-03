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

# h, w = mapInt()
n, s = input().split()

n = int(n)

ans = 0
# ok = ["AT", "CG", "TA", "GC"]
# ok2 = [ "AGCT", "AGTC", "GACT", "GATC", "CTAG", "TCAG", "CTGA", "TCGA"]
# for i in range(2):
#   cnt = 0
#   for j in range(i, n, 2):
#     if s[j: j+2] in ok:
#       cnt += 1
#       # ans += (cnt+1) * (cnt) // 2
#     elif j < n and s[j:j+4] in ok2:
#       cnt += 1
#       j += 2
#       # ans += (cnt+1) * (cnt) // 2
#     else: 
#       ans += (cnt) * (cnt+1) // 2
#       cnt = 0
#     # print(s[j: j+2], s[j:j+4])
#   ans += (cnt) * (cnt+1) // 2
#   # print(ans)
# print(ans)

a = [0] *(n+1)
t = [0] *(n+1)
c = [0] *(n+1)
g = [0] *(n+1)

for i in range(n):
  a[i+1] = a[i]
  t[i+1] = t[i]
  c[i+1] = c[i]
  g[i+1] = g[i]

  if s[i] == "A":
    a[i+1] +=1
  if s[i] == "T":
    t[i+1] +=1
  if s[i] == "C":
    c[i+1] +=1
  if s[i] == "G":
    g[i+1] +=1
    

for i in range(n):
  for j in range(i+1, n+1):
    # print(a[j], a[i], j , i)
    if (a[j] - a[i] == t[j] - t[i]) and (c[j] - c[i] == g[j] - g[i]):
      ans += 1
print(ans)