# -*- coding: utf-8 -*-
from re import L
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
inithw = lambda h: [ list(input()) for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]

YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1
from operator import itemgetter
from collections import defaultdict
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
      
      
      

# 残念こーど
# l = input()
# n = len(l)
# cnt = 0

# if n == 1:
#     print(3)
#     sys.exit()

# for i in range(1, n):
#     if l[i] == "1":
#         cnt += 1

    


# ans = ModInt(3)

# for i in range(1, n-1):
#     ans += ModInt(2* (3**i))

# # print(ans, n, cnt)
# ans += ModInt(2 * (3**cnt))
# print(ans)


l = input()
n = len(l)

# dp[i][j]i番目の桁が確定した時の場合のかず# j: 0 or 1, 0の時は以下なんでも良い, 1の時はそこまで一致している時
dp = [ [0, 0] for _ in range(n+1)]
dp[0][0] = 0
dp[0][1] = 1

for i in range(1, n+1):
        # i桁目が1の時
        if l[i-1] == "1":
            # (0, 0) (0, 1), (1, 0)
            dp[i][0] = dp[i-1][0] * 3 + dp[i-1][1] * 1
            # (0, 1) or (1, 0)
            dp[i][1] = (dp[i-1][1]) * 2
        else: # i桁目が0の時
            # (0, 0) (0, 1) (1, 0)
            dp[i][0] = (dp[i-1][0]) * 3
            # (0, 0)
            dp[i][1] = (dp[i-1][1]) * 1
        dp[i][0] %= MOD
        dp[i][1] %= MOD
        
# print(dp)
print((dp[n][0] + dp[n][1]) % MOD)
