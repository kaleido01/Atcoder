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
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
# YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

n = int(input())
s = input()

lis = []

for i in range(len(s)):
  lis.append((s[i], -1 * i))

# lis.sort(key= lambda x: x[1], reverse= True)
lis.sort()
# print(lis)
cur = 0
last = INF

change =[]
for i in range(len(s)):
  t = s[i]
  temp = 0
  if last <= i: break
  if t <= lis[temp][0]: continue
  # 使える後ろが今見ているiより大きい　かつ　alphabetが今見ているindexより大きい もしくは最後に交換した場所よりも大きい
  while(temp <= n-1 and (last <= -1 * lis[temp][1])):
    temp += 1
  # print(-1 * lis[cur][1], i)
  # print(last, -1*lis[temp][1], t, lis[temp][0])
  if temp <= n-1 and last > -1 * lis[temp][1] and t > lis[temp][0] and i < -1 * lis[temp][1]:
    change.append((i, -1 * lis[temp][1]))
    last = -1 * lis[temp][1]
    # cur = 
  else:
    break

s = list(s)
# print(change)
for temp1, temp2 in change:
  s[temp1], s[temp2] = s[temp2], s[temp1]

print("".join(s))

  


# print("".join(top) + "".join(end.reverse()))