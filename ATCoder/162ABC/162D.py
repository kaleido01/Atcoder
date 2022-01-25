# -*- coding: utf-8 -*-
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7 # 998244353
d4 = [(0,1), (1,0)]
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

n = int(input())
s = input()

r = [0] * (n+1)
g = [0] * (n+1)
b = [0] * (n+1)


for i in range(n):
  if s[i] == "R":
    r[i+1] = r[i] + 1
    g[i+1] = g[i]
    b[i+1] = b[i]
  elif s[i] == "G":
    r[i+1] = r[i]
    g[i+1] = g[i] + 1
    b[i+1] = b[i]
  else:
    r[i+1] = r[i]
    g[i+1] = g[i]
    b[i+1] = b[i] + 1

ans = 0
for i in range(n-2):
  for j in range(i+1, n-1):
    # print(i, j, 2*j-i)
    if s[i] == s[j]: continue
    
    if (s[i] == "R" and s[j] == "G") or (s[i] == "G" and s[j] == "R") :
      ans += b[n] - b[j]
      if 2*j-i < n and s[2*j-i] == "B":
        ans -= 1
    elif (s[i] == "G" and s[j] == "B") or (s[i] == "B" and s[j] == "G"):
      ans += r[n] - r[j]
      if 2*j-i < n and s[2*j-i] == "R":
        ans -= 1
    else:
      ans += g[n] - g[j]
      if 2*j-i < n and s[2*j-i] == "G":
        ans -= 1
  
  
print(ans)