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

lis = [ [] for i in range(26)]

for i in range(n):
  
  heapq.heappush(lis[ord(s[i]) - ord('a')], -1 * i)
  
# print(lis)
last = INF
change = []
for i in range(n // 2):
  t = s[i]
  cur = 0
  while(cur < 26 and cur < ord(t) - ord('a')):
    ok = False
    while(lis[cur]):
      # print(cur)
      okIndex = -1 * heapq.heappop(lis[cur])
      if okIndex < last and i < okIndex:
        last = okIndex
        change.append((i, okIndex))
        ok = True
        break
    if ok: break        
    cur += 1


s = list(s)
# print(change)
for temp1, temp2 in change:
  s[temp1], s[temp2] = s[temp2], s[temp1]

print("".join(s))
    