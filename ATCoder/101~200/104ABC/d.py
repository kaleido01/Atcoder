# -*- coding: utf-8 -*-
from ast import Mod
from operator import mod
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
class ModInt:
  MOD = 10**9 +7
  def __init__(self, x):
      self.x = x % MOD

  def __str__(self):
      return str(self.x)

  __repr__ = __str__

  def __add__(self, other):
      return (
          ModInt(self.x + other.x) if isinstance(other, ModInt) else
          ModInt(self.x + other)
      )

  def __sub__(self, other):
      return (
          ModInt(self.x - other.x) if isinstance(other, ModInt) else
          ModInt(self.x - other)
      )

  def __mul__(self, other):
      return (
          ModInt(self.x * other.x) if isinstance(other, ModInt) else
          ModInt(self.x * other)
      )

  def __truediv__(self, other):
      return (
          ModInt(
              self.x * pow(other.x, MOD - 2, MOD)
          ) if isinstance(other, ModInt) else
          ModInt(self.x * pow(other, MOD - 2, MOD))
      )

  def __pow__(self, other):
      return (
          ModInt(pow(self.x, other.x, MOD)) if isinstance(other, ModInt) else
          ModInt(pow(self.x, other, MOD))
      )

  __radd__ = __add__

  def __rsub__(self, other):
      return (
          ModInt(other.x - self.x) if isinstance(other, ModInt) else
          ModInt(other - self.x)
      )

  __rmul__ = __mul__

  def __rtruediv__(self, other):
      return (
          ModInt(
              other.x * pow(self.x, MOD - 2, MOD)
          ) if isinstance(other, ModInt) else
          ModInt(other * pow(self.x, MOD - 2, MOD))
      )

  def __rpow__(self, other):
      return (
          ModInt(pow(other.x, self.x, MOD)) if isinstance(other, ModInt) else
          ModInt(pow(other, self.x, MOD))
      )
      
      
      


s = input()
n = len(s)
sl = [0] * (n+1)
sr = [0] * (n+1)
lq = [0] * (n+1)
rq = [0] * (n+1)

for i in range(n):
  sl[i+1] = sl[i]
  sr[i+1] = sr[i]
  lq[i+1] = lq[i]
  rq[i+1] = rq[i]
  
  if s[i] == "A":
    sl[i+1] +=1

  if s[i] == "?":
    lq[i+1] += 1

  if s[n-i-1] == "C":
    sr[i+1] +=1
  if s[n-i-1] == "?":
    rq[i+1] +=1
    
    
    
  
ans = ModInt(0)
# print(sl,sr, lq, rq)
for i in range(1, n-1):
  if s[i] == "B" or s[i] == "?":
    # print("aaa", lq[i], sl[i], rq[n-i-1], sr[n-i-1])
    left = 0
    right = 0
    if lq[i] >=1:
      # left = ModInt(3 ** lq[i] * sl[i] + 3 ** (lq[i]-1)* lq[i])
      left = ModInt(3*sl[i]+lq[i])* (ModInt(3) ** (lq[i]-1))
    else:
      left = ModInt(sl[i])
    if rq[n-i-1] >=1:
      # right = ModInt(3 ** rq[n-i-1] * sr[n-i-1] + 3 ** (rq[n-i-1]-1) * rq[n-i-1])
      right = ModInt(3*sr[n-i-1]+rq[n-i-1]) * (ModInt(3) ** (rq[n-i-1]-1))
    else:
      right = ModInt(sr[n-i-1])
      
      
    # print(left, right)
    ans += left * right
    
  
print(ans)