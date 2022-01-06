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

n,k,p= mapInt()

an = listInt()
bn = an[:n // 2]
cn = an[n//2:]
dn = [[] for i in range(21)]
en = [[] for i in range(21)]
for i in range(2 ** (n//2)):
  s = 0
  counter = 0
  for j in range(n//2):
    if (i >> j) & 1:
      s += bn[j]
      counter += 1
  dn[counter].append(s)


ans = 0
for i in range(2 ** ((n+1)//2)):
  s = 0
  counter = 0
  for j in range((n+1)//2):
    if (i >> j) & 1:
      s += cn[j]
      counter += 1
  en[counter].append(s)
  
for i in range(len(en)):
  en[i].sort()

ans = 0


def isOk(index, key, i):
  # print(index, key, i)
  # print(en[k-i][index], key)
  return en[k-i][index] <= key


# print(dn, en)
for i in range(len(dn)):
  for v in dn[i]:
    if not(0 <= k-i < len(en)): continue
    target = p - v
    ng = -1
    ok = len(en[k-i])
    while(abs(ok-ng) > 1):
      middle = (ok + ng) // 2
      if isOk(middle, target, i):
        ng = middle
      else:
        ok = middle
    
    #left +1が条件をみたす範囲の個数
    # print(target, ok)
    ans += ok
    
    
    
    
print(ans)