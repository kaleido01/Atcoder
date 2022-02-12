# -*- coding: utf-8 -*-
from audioop import lin2adpcm
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
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
# YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1


n = int(input())
aa = listInt()
bb = listInt()
test = []

for i in range(n):
  a = aa[i]
  b = bb[i]
  test.append((a+b, a, i+1))
  
  

test.sort(reverse= True)

ans = []
pq = []
pq2 = []

def push2():
  # print(pq2)
  while pq2:
    num = heapq.heappop(pq2)
    ans.append(num)
  

def push():
  now = 0
  # print(pq)
  while pq:
    a, num = heapq.heappop(pq)
    
    if now != a:
      now = a
      push2()
      heapq.heappush(pq2, (num))
    else:
      heapq.heappush(pq2, (num))
  push2()
      

now = 0
for i in range(n):
  s, a, num = test[i]
  if now != s:
    now = s
    push()
    heapq.heappush(pq, (-a, num))
  else:
    heapq.heappush(pq, (-a, num))

# print(test)
push()
    
print(*ans)