# -*- coding: utf-8 -*-
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
from typing import Awaitable
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7 # 998244353
d4 = [(0,1), (1,0)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
input=lambda: sys.stdin.readline().rstrip()
intInput = lambda: int(input())
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
def divisor_list_s(num):
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            prime[i] = True
            if i**2 == num:
                continue
            prime[int(num/i)] = True
  
  

n, m = mapInt()
a = listInt()

# ng = [0] * (m+1)
ng = [False] * (m+1)
prime = {}
for i in range(n):
  divisor_list_s(a[i])


# print(prime)
for key in prime.keys():
  if key == 1: continue
  for j in range(key, m+1, key):
    ng[j] = True

ans = []
for i in range(1, m+1):
  if not ng[i]:
    ans.append(i)
    
print(len(ans))
for x in ans:
  print(x)