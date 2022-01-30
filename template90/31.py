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

n = int(input())

w = listInt()
b = listInt()

d = [ [-1 for _ in range(1301)] for _ in range(51)]
# d[0][1] = 0

for i in range(51):
  for j in range(1301):
    
    if i == 0 and j <= 1:
      d[i][j] = 0
      continue
    # 白遷移
    used = [False] * 666
    if i >= 1 and i + j <= 1300:
      used[d[i-1][j+i]] = True

    #黒遷移
    for k in range(1, j // 2+1):
      used[d[i][j-k]] = True
      
    temp = 0
    while used[temp]: temp +=1

    d[i][j] = temp

xor = 0
for i in range(n):
  wi = w[i]
  bi = b[i]
  xor ^= d[wi][bi]

# print(d)
if xor == 0:
  print("Second")
else:
  print("First")