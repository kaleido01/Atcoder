# -*- coding: utf-8 -*-
import sys, getpass, string
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

# n = int(input())
# s = input()
# h, w = mapInt()
n, m = mapInt()

s = [0] *(n+1)
a = []
for i in range(n):
  a.append(i * (i+1) //2)
  
for i in range(n):
  s[i+1] = s[i] + a[i]

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])
    return arr

lis = factorization(m)
ans = 1

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
  
c = Combination(200020)

if m == 1:
  print(1)
  exit()
for v, cnt in lis:
  ans *= c.cmb(n+cnt-1, cnt)
  ans %= MOD
print(ans)