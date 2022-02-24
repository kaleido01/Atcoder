# -*- coding: utf-8 -*-
from audioop import lin2adpcm
from lib2to3.pgen2.token import INDENT
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
def gcd(x,y):
  if y==0:     #[1]yが0の時はxを返す
    return x 
  else:#[2]y=0以外の時
    return gcd(y,x%y)

n = int(input())
a = listInt()


s1 = [1] * (n)
s2 = [1] * (n)
s1[0] = a[0]
s2[0] = a[n-1]

for i in range(n-1):
  s1[i+1] = gcd(s1[i], a[i+1])
  s2[i+1] = gcd(s2[i], a[n-i-2])
  
  
ans = 1
# print(s1, s2)
for i in range(n):
  if i == 0:
    y = s2[n-2]
    ans = max(ans, y)
  elif i == n-1:
    x = s1[n-2]
    ans = max(ans, x)
  else:
    x = s1[i-1]
    y = s2[n-i-2]
    ans = max(ans, gcd(x,y))
  
print(ans)