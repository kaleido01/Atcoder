# -*- coding: utf-8 -*-
from operator import mod
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
class Combination:
  mod = 10**9+7 #出力の制限
  g1 = [1, 1] # 元テーブル
  g2 = [1, 1] #逆元テーブル
  inverse = [0, 1] #逆元テーブル計算用テーブル
  
  def __init__(self,n):
    for i in range(2, n + 1 ):
     self.g1.append( ( self.g1[-1] * i ) % self.mod )
     self.inverse.append( ( -self.inverse[self.mod % i] * (self.mod//i) ) % self.mod )
     self.g2.append( (self.g2[-1] * self.inverse[-1]) % self.mod )

  def cmb(self, n, r):
    if ( r < 0 or r > n ):
        return 0
    r = min(r, n - r)
    return self.g1[n] * self.g2[r] * self.g2[n-r] % self.mod
  
  def per(self, n, r):
    if ( r < 0 or r > n ):
        return 0
    return self.g1[n] * self.g2[n-r] % self.mod
n, m = mapInt()




if abs(n-m) >= 2:
  print(0)
  exit()
com = Combination(n+2)


if abs(n-m) == 1:
  v = com.per(n,n) * com.per(m,m)
  v %= MOD
  print(v)
else:
  v = 2 * com.per(n,n) * com.per(m,m)
  v %= MOD
  print(v)

