# -*- coding: utf-8 -*-
import sys, getpass, string
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

a = listInt()
b = listInt()

cntA = {}
cntB = {}

for i in range(n):
  if a[i] in cntA:
    cntA[a[i]] +=1
  else:
    cntA[a[i]] =1
  if b[i] in cntB:
    cntB[b[i]] +=1
  else:
    cntB[b[i]] = 1
    
can = True
double = False
for k, v in cntA.items():
  if v >=2: double = True
  if k in cntB:
    if cntB[k] != v:
      can = False
      break
  else:
    can = False
    break
if not can:
  print("No")
  exit()
  
  
for i in range(n-2):
  target = b[i]
  temp = i
  while(temp < n and a[temp] != target): temp+=1
  # print(a, temp, i)
  if temp == i: continue
  if (temp - i) % 2 == 0:
    pass
  else:
    if temp == n-1:
      a[temp-2], a[temp-1], a[temp] = a[temp-1], a[temp], a[temp-2]
      temp -= 1
    else:
      a[temp-1], a[temp], a[temp+1] = a[temp+1], a[temp-1], a[temp]
      temp +=1
      
  q = deque(a[i:temp+1])
  x = q.pop()
  q.appendleft(x)
  a = a[:i] + list(q) + a[temp+1:]
  # print(a)
  
x, y, z = a[n-3:]
tx, ty, tz = b[n-3:]

if double or (x == tx and y == ty and z == tz) or (x ==ty and y==tz and z == tx) or (x ==tz and y==tx and z == ty):
  print("Yes")
else:
  print("No")

# print(a)