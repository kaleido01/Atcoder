# -*- coding: utf-8 -*-
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect, statistics
from collections import Counter, defaultdict, deque
from operator import add

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

# h, w = mapInt()
# n = int(input())
# a = listInt()

w, n = mapInt()


# テストケース１
# field = [0] * w
# currentM = 0
# for i in range(n):
#   l, r = mapInt()
#   l, r = l-1, r-1
#   m = 0
#   for i in range(l, r+1):
#     m = max(field[i], m)
  
#   for i in range(l, r+1):
#     field[i] = m+1
#   currentM = field[l]
#   print(currentM)
  
# テストケース2
# pressed = []

# field = [0] * w
# currentM = 0

# for i in range(n):
#   l, r = mapInt()
#   pressed.append([l, r])

  
# B = sorted(set(list(itertools.chain.from_iterable(pressed))))

# D = { v: i for i, v in enumerate(B) }

# def f(v):
#   x = D[v[0]]
#   y = D[v[1]]
#   # newArray.append((x,y))
#   return [x, y]
# pressed = list(map(f, pressed))
# # print(pressed)
# for i in range(n):
#   l, r = pressed[i]
#   m = 0
#   for j in range(l, r+1):
#     m = max(field[j], m)
  
#   for j in range(l, r+1):
#     field[j] = m+1
#   currentM = field[l]
#   print(currentM)
  
  
  
class LazySegmentTree:
  def __init__(self, op, e, mapping, composition, id_, n):
      _n = len(n) if isinstance(n, list) else n
      self.op = op
      self.e = e
      self.mapping = mapping
      self.composition = composition
      self.id = id_
      self.log = (_n - 1).bit_length()
      self.size = 1 << self.log
      self.d = [e for _ in range(2 * self.size)]
      self.lz = [id_ for _ in range(self.size)]
      if isinstance(n, list): self.d[self.size: self.size + _n] = n
      [self._update(i) for i in reversed(range(1, self.size))]

  def __repr__(self):
      l, r = 1, 2
      res = []
      np_T = lambda x: [list(x) for x in zip(*x)]
      while r <= self.size:
          res.append(f'{np_T([self.d[l: r], self.lz[l: r]])}')
          l, r = r, r << 1
      res.append(f'{self.d[l: r]}')
      return '\n'.join(res)

  def set(self, p, x):
      p += self.size
      [self._push(p >> i) for i in reversed(range(1, self.log + 1))]
      self.d[p] = x
      [self._update(p >> i) for i in range(1, self.log + 1)]

  def get(self, p):
      p += self.size
      [self._push(p >> i) for i in reversed(range(1, self.log + 1))]
      return self.d[p]

  def prod(self, l, r):
      if l == r: return self.e
      l += self.size
      r += self.size
      for i in reversed(range(1, self.log + 1)):
          if ((l >> i) << i) != l: self._push(l >> i)
          if ((r >> i) << i) != r: self._push((r - 1) >> i)
      sml, smr = self.e, self.e
      while (l < r):
          if l & 1:
              sml = self.op(sml, self.d[l])
              l += 1
          if r & 1:
              r -= 1
              smr = self.op(self.d[r], smr)
          l >>= 1;
          r >>= 1;
      return self.op(sml, smr)

  def all_prod(self):
      return self.d[1]

  def apply(self, p, f):
      p += self.size;
      [self._push(p >> i) for i in reversed(range(1, self.log + 1))]
      self.d[p] = mapping(f, self.d[p]);
      [self._update(p >> i) for i in range(1, self.log + 1)]

  def apply_seg(self, l, r, f):
      if l == r: return
      l += self.size;
      r += self.size;
      for i in reversed(range(1, self.log + 1)):
          if ((l >> i) << i) != l: self._push(l >> i)
          if ((r >> i) << i) != r: self._push((r - 1) >> i)
      l2, r2 = l, r
      while l < r:
          if l & 1:
              self._all_apply(l, f);
              l += 1
          if r & 1:
              r -= 1
              self._all_apply(r, f);
          l >>= 1;
          r >>= 1;
      l, r = l2, r2
      for i in range(1, self.log + 1):
          if ((l >> i) << i) != l: self._update(l >> i)
          if ((r >> i) << i) != r: self._update((r - 1) >> i)

  def _update(self, k):
      self.d[k] = self.op(self.d[2 * k], self.d[2 * k + 1])

  def _all_apply(self, k, f):
      self.d[k] = self.mapping(f, self.d[k])
      if k < self.size: self.lz[k] = self.composition(f, self.lz[k])

  def _push(self, k):
      self._all_apply(2 * k, self.lz[k])
      self._all_apply(2 * k + 1, self.lz[k])
      self.lz[k] = self.id

# W = [0] * n
f = lambda x, y: y if x == INF else x

# seg = LazySegmentTree(min, INF, f, f, INF, W)  # 区間更新・区間最小値取得
seg = LazySegmentTree(max, -INF, f, f, INF, w)  # 区間更新・区間最大値取得
# seg = LazySegmentTree(min, INF, add, add, 0, W)  # 区間加算・区間最小値取得
# seg = LazySegmentTree(max, -INF, add, add, 0, w)  # 区間加算・区間最大値取得
# seg = LazySegmentTree(segadd, (0, 0), lambda f, x: (x[0] + f * x[1], x[1]), add, 0, [(0, 1) for _ in range(W)])  # 区間加算・区間和取得
# seg = LazySegmentTree(segadd, (0, 0), lambda f, x: (f * x[1], x[1]) if f < INF else x, f, INF, [(0, 1) for _ in range(W)])  # 区間更新・区間和取得

seg.apply_seg(0, w, 0)
# print(seg.d)
for i in range(n):
  l, r = mapInt()
  # print(l, r)
  height = seg.prod(l - 1, r) + 1
  seg.apply_seg(l - 1, r, height)
  print(height)
    