


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
n, p, k = mapInt()

temp  = [[0 for  _ in range(n)] for _ in range(n)]

for i in range(n):
  ai = listInt()
  for j in range(n):
    temp[i][j] = ai[j]

def war(X):
  dp = [[math.inf for  _ in range(n)] for _ in range(n)]
  for i in range(n):
    for j in range(n):
      if temp[i][j] == -1:
        dp[i][j] = X
      else:
        dp[i][j] = temp[i][j]
  for k in range(n):
    for i in range(n):
      for j in range(n):
        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
  cnt = 0
  for i in range(n-1):
    for j in range(i+1, n):
      if dp[i][j] <= p:
        cnt += 1
  return cnt


# print(war(1))
# print(war(2))
# print(war(3))
# print(war(4))
# print(war(5))

def isOk(index, boundary):
  """不等号を入れ替える場合は呼び出し側のOKとNGのmiddleも入れ替える"""
  x = war(index)
  return boundary >= x
  # return a[index] >= key

def isOk1(index, boundary):
  """不等号を入れ替える場合は呼び出し側のOKとNGのmiddleも入れ替える"""
  x = war(index)
  return boundary > x

def binary_search(v, isMin):
    ok = 10 ** 12
    ng = 0
    while(abs(ok-ng) > 1):
      middle = (ok + ng) // 2
      if isMin:
        if isOk(middle, v):
          ok = middle
        else:
          ng = middle
      else:
        if isOk1(middle, v):
          ok = middle
        else:
          ng = middle
    return ok
        
      
    

if war(p+1)>k:
  print(0)
  sys.exit()
if war(p+1)==k:
  print("Infinity")
  sys.exit()

## 5
minimum = binary_search(k, True)
maximum = binary_search(k, False)

if maximum == minimum == 10**12:
  print("Infinity")
elif maximum == 10**12:
  print("Infinity")
else:
  print(maximum - minimum)
  
# print(minimum, maximum)