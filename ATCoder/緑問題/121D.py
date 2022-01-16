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


a, b = mapInt()

maxn = 0

temp = b

while temp:
  temp //= 2
  maxn += 1

# print(maxn)
# 逆順で入る
ans = []
for i in range(maxn):
  cn = 2 ** i
  mina = max(a, cn)
  diffa = (mina - cn) % (2 * cn)
  diffb = (b+1-cn) % (2 * cn)
  if i == 0:
    if a % 2 == 1:
      x = (b-a+1) % 4
      if x == 1 or x == 2:
        ans.append(1)
      else:
        ans.append(0)
    else:
      x = (b-a+1) % 4
      if x == 2 or x == 3:
        ans.append(1)
      else:
        ans.append(0)
    continue
    
    
  # print(mina, diffa, diffb)
  cnt1 = 0
  if diffa // cn == 1:
    # 1の数は偶数
    pass
  else:
    cnt1 += cn - (diffa % cn)
    
  if diffb // cn == 1:
    # 1の数は偶数
    pass
  else:
    cnt1 += diffb % cn

  # print("cnt1", cnt1)
  if cnt1 % 2 == 1:
    ans.append(1)
  else:
    ans.append(0)
    
# ans.reverse()
# print(ans)
a = 0
for i in range(len(ans)):
  a += ans[i] * 2**i

print(a)
  
  
  
  