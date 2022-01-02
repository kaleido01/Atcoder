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


n, l = mapInt()
k = int(input())
a = listInt()
a.append(l)
s = init0(n+1)
s[0] = a[0]
for i in range(1, n+1):
  s[i] = a[i] - a[i-1] 

#　二分探索
# print(s)



def isOk(index, key):
  return a[index] >= key

def binary_search(v):
  left = -1
  right = len(a)
  
  while(right - left >1):
    # middle = left + (left - right)//2
    middle = (left + right)//2
    if isOk(middle, v):
      right = middle
    else:
      left = middle
  return right



def ok(middle):
  ans = 0
  count = 0
  for i in range(n+1):
    ans += s[i]
    if ans >= middle:
      if count == k:
        pass
      else:
        ans = 0
        count += 1
  # print(ans, count, middle)
  return ans >= middle and count >= k


left= -1
right = 10 ** 9
while(right - left > 1):
  middle = (left+right) // 2
  if (ok(middle)):
    left = middle
  else:
    right = middle



print(left)
