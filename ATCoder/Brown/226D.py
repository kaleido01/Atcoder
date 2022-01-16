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

grid = []

for i in range(n):
  grid.append(listInt())
  

ans = {}

def gcd(x,y):
  if y==0:     #[1]yが0の時はxを返す
    return x 
  else:#[2]y=0以外の時
    return gcd(y,x%y)

for i in range(n):
  for j in range(n):
    if i == j: continue
    x1 = grid[i][0]
    y1 = grid[i][1]
    x2 = grid[j][0]
    y2 = grid[j][1]
    
    d1 = x2 - x1
    d2 = y2 - y1
    r = gcd(d1,d2)
    # print(r)
    # print(d1 // r, d2 // r)
    ans[(d1 // abs(r), d2 // abs(r))] = True

print(len(ans.keys()))
    