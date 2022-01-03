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
inithw = lambda h: [ list(input()) for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]
bit = lambda n, k:((n >> k) & 1) # nのkビット目
# YesNo=lambda b: bool([print('Yes')] if b else print('No'))
# YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

# h, w = mapInt()
# n = int(input())
# a = listInt()

w, n = mapInt()


# テストケース１
# field = [0] * w
# currentM = 0
# for i in range(n):
#   l, r = mapInt()
#   l, r = l-1, r-1
#   m = 0
#   for i in range(l, r+1):
#     m = max(field[i], m)
  
#   for i in range(l, r+1):
#     field[i] = m+1
#   currentM = field[l]
#   print(currentM)
  
  
pressed = []

field = [0] * w
currentM = 0

for i in range(n):
  l, r = mapInt()
  pressed.append([l, r])

  
B = sorted(set(list(itertools.chain.from_iterable(pressed))))

D = { v: i for i, v in enumerate(B) }

def f(v):
  x = D[v[0]]
  y = D[v[1]]
  # newArray.append((x,y))
  return [x, y]
pressed = list(map(f, pressed))
# print(pressed)
for i in range(n):
  l, r = pressed[i]
  m = 0
  for j in range(l, r+1):
    m = max(field[j], m)
  
  for j in range(l, r+1):
    field[j] = m+1
  currentM = field[l]
  print(currentM)