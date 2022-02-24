# -*- coding: utf-8 -*-
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
from urllib.parse import MAX_CACHE_SIZE
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
s = listInt()

a = [0] * (n+2)
a[0] = 0
a[1] = 0
a[2] = s[0]

for i in range(3, n+2):
  # if i % 3 == 0:
  #   s[i] = s[i-2] + a[i+1] - a[i]
  # elif i % 3 == 1:
  #   s[i] = s[i-2] + a[i+1] - a[i]
  # else:
  # print(i)
  a[i] = a[i-3] + s[i-2] - s[i-3]
    
    

c3 = INF

minA = 0
minB = 0
for i in range(n+2):
  # print(a[i]+a[i+1], a[i+2])
  if i % 3 == 0:
    minA = max(minA, -a[i])
    if i+1 < n+2:
      minB = max(minB, -a[i+1])
    if i+2 < n+2:
      c3 = min(c3, a[i+2])
    if minA + minB > c3:
      print("No")
      exit()
  # print(c1c2, c3)

  

# print(minA, minB)
# print(a)
ans = []
ans.append(minA)
ans.append(minB)
ans.append(a[2]-ans[0]-ans[1])
for i in range(3, n+2):
  if (i+1) % 3 == 0:
    ans.append(a[i]-minA-minB)
  elif (i+1) % 3 == 1:
    ans.append(a[i]+minA)
  else:
    ans.append(a[i]+minB)

print("Yes")
print(*ans)