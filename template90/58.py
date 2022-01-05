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

n, k = mapInt()


d = {}
temp = str(n)
w =[]
s = 0
for v in temp:
  s += int(v)


d[n] = 0
w.append(n)
temp = (int(temp) + s) % 10**5
d[temp] = 1
w.append(temp)
count = 2
while(count <= k):  
  s = 0
  for v in str(temp):
    s += int(v)
  
  temp = (int(temp) + s) % 10**5
  if temp in d.keys():
    break
  else:
    d[temp] = count
    w.append(temp)

    count += 1
    # print(count)
  # print(n, temp)
  # if n == temp:
  #   print("aaa")
  #   break
  
if count == k+1:
  print(temp)
else:
  roop = d[temp]
  # print(roop)
  # if temp == d[0]:
  rest = (k - roop) % (count - roop)
  print(w[roop + rest])
  # else:
  #   rest = k %(count-1)
  #   print(d[rest])
# print(count, temp)
# print(count, temp)
# rest = k % (count-1)
# print(