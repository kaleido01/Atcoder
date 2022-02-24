# -*- coding: utf-8 -*-
from re import L
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

a = listInt()


s = [ [ 0 for i in range(n+1)] for i in range(20)]


for i in range(20):
  for j in range(n):
    if (a[j] >> i) & 1:
      s[i][j+1] = s[i][j] + 1
    else:
      s[i][j+1] = s[i][j]
      

ans = 0
right = 0
def isOk(left, right):
  
  ok = True
  for i in range(20):
    # print(left, right)
    if s[i][right] - s[i][left] > 1:
      ok = False
      break
  return ok
  
for left in range(n+1):
  while(right < n+1 and  isOk(left, right)):
    right +=1
    
  ans += right - left -1
  
print(ans)