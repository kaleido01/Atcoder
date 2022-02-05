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
initAny = lambda n, a: [a for _ in range(n)]


inithwv = lambda h, w, v: [[v for _ in range(w)] for _ in range(h)]
inithw = lambda h: [ list(input()) for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]
bit = lambda n, k:((n >> k) & 1) # nのkビット目
# YesNo=lambda b: bool([print('Yes')] if b else print('No'))
# YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

# h, w = mapInt()
n, m = mapInt()



a = listInt()


pq = []
dic = {}

for i in range(n):
  if a[i] in dic:
    dic[a[i]] +=1
  else:
    dic[a[i]] =1

for k, v in dic.items():
  heapq.heappush(pq, (k, v))


for i in range(m):
  b, c = mapInt()
  
  cnt = 0
  while(len(pq) > 0 and cnt < b):
    # print(pq)
    index, count = heapq.heappop(pq)
    if c <= index: 
      heapq.heappush(pq, (index, count))
      break
    if cnt + count > b:
      count -= b - cnt
      heapq.heappush(pq, (index, count))
      cnt = b
    else:
      cnt += count
  # print(cnt, c)
  if cnt > 0:
    heapq.heappush(pq, (c, cnt))

ans = 0
# print(pq)
while pq:
  index, count = heapq.heappop(pq)
  ans += index * count
  
print(ans)