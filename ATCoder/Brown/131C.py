# -*- coding: utf-8 -*-
from re import L
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

a, b, c, d = mapInt()

def gcd(x,y):
  if y==0:     #[1]yが0の時はxを返す
    return x 
  else:#[2]y=0以外の時
    return gcd(y,x%y)

# x = b // c
# y = b // d

# p = gcd(c,d)

# mincd = c * d // p
# # print(mincd)
# z = b // mincd

# l = (a-1) // c
# m = (a-1) // d
# n = (a-1) // mincd

# ok = (x+y-z) - (l+m-n)
# print(b - a + 1 - ok)

def f(x):
  p = x // c
  q = x // d
  
  r = gcd(c, d)
  z = c * d // r
  s = x // z
  return x-(p+q - s)

print(f(b) - f(a-1))