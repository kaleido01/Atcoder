# -*- coding: utf-8 -*-
import sys, getpass, string
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
sys.setrecursionlimit(10**5)
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

n = int(input())
# s = input()
# h, w = mapInt()

s = [list(input()) for i in range(n)]

# print(s)
# tate
x =[ [0 for i in range(n+1)] for i in range(n)]
y =[ [0 for i in range(n)]  for i in range(n+1)]

for i in range(n):
  for j in range(n):
    x[i][j+1] = x[i][j]
    if s[i][j] == "#":
      x[i][j+1] +=1

    
for j in range(n):
  for i in range(n):
    y[i+1][j] = y[i][j]
    if s[i][j] == "#":
      y[i+1][j] +=1
    

can = False

for i in range(n):
  for j in range(1, n-4):
    # print(x[i][j+5] - x[i][j-1])
    if x[i][j+5] - x[i][j-1] >= 4:
      can = True
      
for j in range(n):
  for i in range(1, n-4):
    if y[i+5][j] - y[i-1][j] >= 4:
      can = True
            
for i in range(n-6, -1, -1):
  for k in range(n):
    if not k + 5 < n: break
    if not i + k + 5 < n: break
    p = 0
    for v in range(6):
      if s[i + k + v][k+v] == "#":
        # print(s[i+k][j+k])
        p += 1
    if p >= 4:
      can = True
      
for j in range(n-6, -1, -1):
  for k in range(n):
    if not k + 5 < n: break
    if not j + k + 5 < n: break
    p = 0
    for v in range(6):
      if s[k + v][j+k+v] == "#":
        # print(s[i+k][j+k])
        p += 1
    if p >= 4:
      can = True
      
for i in range(5, n):
  for k in range(n):
    if not k + 5 < n: break
    if not i - k - 5 >=0 : break
    p = 0
    for v in range(6):
      if s[i - k - v][k+v] == "#":
        # print(s[i+k][j+k])
        p += 1
    if p >= 4:
      can = True
      
for j in range(5, n):
  for k in range(n):
    if not k + 5 < n: break
    if not j - k - 5 >= 0: break
    p = 0
    for v in range(6):
      if s[k + v][j-k-v] == "#":
        # print(s[i+k][j+k])
        p += 1
    if p >= 4:
      can = True
      
      
# print(x)
# print(y)
YesNo(can)