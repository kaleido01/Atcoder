# -*- coding: utf-8 -*-
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect, statistics
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


class SegmentTree:
    def __init__(self, op, e, n):
        _n = len(n) if isinstance(n, list) else n
        self.op = op
        self.e = e
        self.log = (_n - 1).bit_length()
        self.size = 1 << self.log
        self.d = [e for _ in range(2 * self.size)]
        if isinstance(n, list): self.d[self.size: self.size + _n] = n
        [self._update(i) for i in reversed(range(1, self.size))]

    def __repr__(self):
        l, r = 1, 2
        res = []
        while r <= 2 * self.size:
            res.append(f'{self.d[l: r]}')
            l, r = r, r << 1
        return '\n'.join(res)

    def set(self, p, x):
        p += self.size
        self.d[p] = x
        [self._update(p >> i) for i in range(1, self.log + 1)]

    def get(self, p):
        return self.d[p + self.size]

    def prod(self, l, r):
        sml, smr = self.e, self.e
        l += self.size;
        r += self.size;
        while (l < r):
            if (l & 1):
                sml = self.op(sml, self.d[l])
                l += 1
            if (r & 1):
                r -= 1
                smr = self.op(self.d[r], smr)
            l >>= 1
            r >>= 1
        return self.op(sml, smr)

    def all_prod(self):
        return self.d[1]

    def _update(self, k):
        self.d[k] = self.op(self.d[2 * k], self.d[2 * k + 1])


# h, w = mapInt()
w, n = mapInt()

g = []

for i in range(n):
  g.append(listInt())
  
dp = inithwv(n+1,w+1,0)
v = [-1] * (w+1)
tree = SegmentTree


for i in range(n):
  for j in range(w+1):
    l, r, v = g[i]
    tree.update(j, )
    # if j-l >= 0 and j-l+r < w:
    if j-l >= 0:
      dp[i+1][j] = max(dp[i][j], dp[i+1][j-l] + v)
    else:
      dp[i+1][j] = dp[i][j]
      

    
print(dp)
print(dp[n][w])