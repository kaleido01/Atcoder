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

n = int(input())

a = listInt()

dic  = {}

for i in range(n):
  if a[i] in dic:
    dic[a[i]] +=1
  else:
    dic[a[i]] =1


pq = []

for k, v in dic.items():
  heapq.heappush(pq, -v)


if len(pq) == 1:
  print(1)
  exit()

while(len(pq) > 1):
  f = heapq.heappop(pq)
  s = heapq.heappop(pq)
  # print(f,s)
  if -f == 1 and -s == 1:
    heapq.heappush(pq,f)
    heapq.heappush(pq,s)
    break
  heapq.heappush(pq,f + 1)
  
  
  if -s == 1:  continue
  heapq.heappush(pq,s + 1)
  
ans = 0
# print(pq)
for i in range(len(pq)):
  ans += -pq[i]
  
print(ans)
