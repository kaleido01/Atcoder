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
inithwv = lambda h, w, v: [[v for _ in range(w)] for _ in range(h)]
inithw = lambda h: [ list(input()) for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]
bit = lambda n, k:((n >> k) & 1) # nのkビット目
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

a, b, Q = mapInt()

s = []
t = []
for i in range(a):
  s.append(int(input()))
for i in range(b):
  t.append(int(input()))


query = []
for i in range(Q):
  query.append(int(input()))
  
  
  
  
  
def isOkS(index, key):
  """不等号を入れ替える場合は呼び出し側のOKとNGのmiddleも入れ替える"""
  return s[index] >= key
def isOkT(index, key):
  """不等号を入れ替える場合は呼び出し側のOKとNGのmiddleも入れ替える"""
  return t[index] >= key


def binary_searchS(v):
    ng = -1
    ok = len(s)
    while(abs(ok-ng) > 1):
      middle = (ok + ng) // 2
      if isOkS(middle, v):
        ok = middle
      else:
        ng = middle
    return ok
def binary_searchT(v):
    ng = -1
    ok = len(t)
    while(abs(ok-ng) > 1):
      middle = (ok + ng) // 2
      if isOkT(middle, v):
        ok = middle
      else:
        ng = middle
    return ok
  
def solve(x):
  ans = INF
  
  # s->t
  ok = binary_searchS(x)
  px = [-1, -1]
  if ok == 0:
    px[0] = s[0]
  elif ok == len(s):
    px[0] = s[-1]
  else:
    px[0] = s[ok]
    px[1] = s[ok-1]
  
  for y in px:
    temp = 0
    if y == -1: continue
    ok = binary_searchT(y)
    if ok == 0:
      temp += abs(x - y)
      temp += abs(y-t[0])
      # print("kkkkkkk",temp)
      ans = min(ans, temp)
    elif ok == len(t):
      temp += abs(x - y)
      temp += abs(y-t[-1])
      ans = min(ans, temp)
    else:
      temp += abs(x - y)
      # print("kkkkkkkaaaa",temp)
      ans = min(ans, temp + abs(y-t[ok]), temp + abs(y-t[ok-1]))
      
  
  # t->s
  ok = binary_searchT(x)
  px = [-1, -1]
  if ok == 0:
    # temp += abs(x - t[0])
    px[0] = t[0]
  elif ok == len(t):
    # temp += abs(x-t[-1])
    px[0] = t[-1]
  else:
    px[0] = t[ok]
    px[1] = t[ok-1]
  
  for y in px:
    temp = 0
    if y == -1: continue
    ok = binary_searchS(y)
    if ok == 0:
      temp += abs(x - y)
      temp += abs(y-s[0])
      ans = min(ans, temp)
    elif ok == len(s):
      temp += abs(x - y)
      temp += abs(y-s[-1])
      ans = min(ans, temp)
    else:
      temp += abs(x - y)
      ans = min(ans, temp + abs(y-s[ok]), temp + abs(y-s[ok-1]))
  
  print(ans)

for x in query:
  solve(x)