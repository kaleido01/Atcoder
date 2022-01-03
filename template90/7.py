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


b = []
c = {}
d = init0(q)
for i in range(q):
  x = int(input())
  b.append(x)
  if x in c:
    c[x].append(i)
  else:
    c[x] = [i]
  
a.append(INF)

a.sort()
b.sort()
# print(a)
# print(b)
index = 0

for i in range(q):

  done = False
  while(not done):
    # if index +1 == len(a):
    #   x = abs(a[index] - b[i])
    #   # print(x)
    #   before = c[b[i]]
    #   d[before] = x
    #   done = True
    #   continue
      
    if b[i] <= a[index] and b[i] <= a[index+1]:
      # print(a[index]-b[i])
      before = c[b[i]]
      for v in before:
        d[v] = a[index]-b[i]
      done = True
      # print("1")

    elif a[index] <= b[i] <= a[index+1]:
      x = b[i] - a[index]
      y = a[index+1] - b[i]
      # print(min(x,y))
      before = c[b[i]]

      for v in before:
        d[v] = min(x,y)
      done = True
      # print("2")]
    
    # elif a[index] <= b[i] and a[index+1] <= b[i] and b[i] <= a[index+2]:
    #   print(b[i] - a[index+1])
    #   done = True
    #   print("3", index, i)

    else:
      index += 1
      

for ans in d:
  print(ans)