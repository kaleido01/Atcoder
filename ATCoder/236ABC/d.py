# -*- coding: utf-8 -*-
from ast import Compare
from calendar import c
from pickle import TRUE
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
mapInt = lambda: map(int, input().split())
listInt = lambda: list(map(int, input().split()))

init0 = lambda n: [0 for _ in range(n)]
inithwv = lambda h, w, v: [[v for _ in range(w)] for _ in range(h)]
inithw = lambda h, w: [ listInt() for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]

YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1
from operator import itemgetter

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
  
  
# c = Combination(120)

# pairs = c.cmb(16, 2)
# print(pairs)

# pattern = c.cmb(pairs, 8)
# print(pattern)


n = int(input())
value = [ [-1 for i in range(2*n)] for i in range(2 * n)]

for i in range(2*n-1):
  a = listInt()
  for j in range(len(a)):
    value[i][i+j+1] = a[j]
    value[i+j+1][i] = a[j]
  
#組み合わせパターン生成
l = [i for i in range(n)]
c_list1 = list(itertools.permutations(l))
c_list2 = list(itertools.permutations(l))

# pattern = list(itertools.combinations(c_list, n))
# print(c_list, pattern)
print(c_list1)
print(c_list2)


for i in range(n):
  for j in range(n):
    print(c_list1)