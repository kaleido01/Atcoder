# -*- coding: utf-8 -*-
from ctypes import Union
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
from tokenize import group
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
      
      
      
n = int(input())

if n==1:
  print(0)
  sys.exit()
elif n==2:
  print(2)
  sys.exit()


ans = ModInt(n) * ModInt(n-1) * ModInt(10**(n-2))
print(ans)

