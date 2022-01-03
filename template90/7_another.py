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

a = listInt()

q = int(input())

a.sort()

def isOk(index, key):
  return a[index] >= key
# def binary_search(v):
#   left = -1
#   right = len(a)
  
#   while(right - left >1):
#     # middle = left + (left - right)//2
#     middle = (left + right)//2
#     if isOk(middle, v):
#       right = middle
#     else:
#       left = middle
#   return right

for i in range(q):
  v = int(input())
  
  left = -1
  right = len(a)
  while(right - left > 1):
    middle = (left + right) // 2
    if isOk(middle, v):
      right = middle
    else:
      left = middle
    # print(left, right)
  
  if left + 1 == len(a):
    x = abs(a[left] - v)
    print(x)
  else:
    x = abs(a[left] - v)
    y = abs(a[right] - v)
    ans = min(x, y)
    print(ans)
    
  