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
n = int(input())

a = listInt()
ans = 0
# for i in range(n):
#   if i+1 != a[i]: continue
#   if i == n-1: 
#     ans+=1
#     print("aaa")
#     break
  
#   # iとi+1でスワップ
#   if i+2 == a[i+1]:
#     ans +=1
#     i+=1
#     if i >= n:break
#     print("hi")
#   else:
#     ans +=1
#     print("a")

i = 0
while i < n:
  if i+1 != a[i]: 
    i +=1
    continue
  if i == n-1: 
    ans+=1
    break
  
  # iとi+1でスワップ
  if i+2 == a[i+1]:
    ans +=1
    i+=2
  else:
    ans +=1
    i +=1
    
print(ans)

    
    
    
    
