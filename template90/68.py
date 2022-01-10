# -*- coding: utf-8 -*-
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect, statistics
from collections import Counter, defaultdict, deque
from typing import Union
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

class UnionFind:
    # 参考 https://note.nkmk.me/python-union-find/
    def __init__(self, n):
        self.parents = [-1] * n   # 負は親（数値は木の大きさ）、非負は子（数値は親インデックス）

    def root(self, x):       # 木の根を求める
        if (self.parents[x] < 0):
            return x
        else:
            self.parents[x] = self.root(self.parents[x])   # 経路圧縮
            return self.parents[x]

    def union(self, x, y):   # 木を結合する
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):       # 木のサイズ
        return -self.parents[self.root(x)]

    def same(self, x, y):    # 同じ木に属するか
        return self.root(x) == self.root(y)

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):   # グループ数
        return len(self.roots())
      






n = int(input())
q = int(input())
ans = []
temp = [0] * n
a = [0] * n
uf = UnionFind(n)
for i in range(q):
  t, x, y, v = mapInt()
  x = x-1
  y = y-1
  if t == 0:
    temp[x] = v
    uf.union(x, y)
  else:
    if not uf.same(x, y):
      ans.append("Ambiguous")
    else:
      ans.append((x, y, v))

for i in range(n-1):
  # if i % 2 == 0:
  # else:
  #   a[i+1] = temp[i] + a[i]
  a[i+1] = temp[i] - a[i]


for i in range(len(ans)):
  if ans[i] == "Ambiguous": continue
  
  x, y, v = ans[i]
  delta = v - a[x]
  if abs(y-x) % 2 == 1:
    ans[i] = a[y] - delta
  else:
    ans[i] = a[y] + delta
  
  
# print(a)
for v in ans:
  print(v)
# print(ans)