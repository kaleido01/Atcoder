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

inithwv = lambda h, w, v: [[v for _ in range(w)] for _ in range(h)]
inithw = lambda h: [ list(input()) for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]
bit = lambda n, k:((n >> k) & 1) # nのkビット目
# YesNo=lambda b: bool([print('Yes')] if b else print('No'))
# YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1
#初期化として考えられる最大のnを入力nCr
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
# h, w = mapInt()

n = int(input())

c = Combination(n)
#差が1->Kまで計算する
for k in range(1, n+1):
  ans = 0
  # a個取得する計算を足し合わせる。ただし、取れる個数が０以下の場合はbreakさせる。
  # 調和級数になるため、このループは高々　n // kしか起こらない
  for a in range(1, n+1):
    if n - (a-1)*(k-1) <= 0: break
    ans += c.cmb(n - (a-1)*(k-1), a)
    ans %= MOD
  print(ans % MOD)
