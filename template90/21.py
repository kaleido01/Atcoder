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
      



n, m = mapInt()

e1 = [[] for _ in range(n)]
e2 = [[] for _ in range(n)]

for i in range(m):
  a, b  = mapInt()
  a, b = a-1, b-1
  
  e1[a].append(b)
  e2[b].append(a)



f = [-1] * n
done = [False] * n
# 帰りがけで順番を記録
def dfs1(start, pos = 0):
  edges = e1[start]
  
  # hasNext = False
  for edge in edges:
    if done[edge]: continue
    done[edge] = True
    # hasNext = True
    pos = dfs1(edge, pos)
  # if not hasNext:
  f[pos] = start
  pos += 1
  return pos


groups = []
done1 = [False] * n
def dfs2(start, group = []):
  edges = e2[start]
  group.append(start)

  for edge in edges:
    if done1[edge]: continue
    done1[edge] = True
    group = dfs2(edge, group)
  return group

pos = 0
#頂点を辿る順を記録する
for i in range(n):
  if done[i]: continue
  done[i] = True
  
  pos = dfs1(i, pos)


# グループ分け
f.reverse()
for i in f:
  if done1[i]: continue
  done1[i] = True
  
  group = dfs2(i, [])
  groups.append(group)


# print(f)
# print(groups)


ans = 0
for group in groups:
  # print(uf.size(i))
  x = len(group)
  ans += x * (x-1) // 2
  # uf.parents[2]
# for i in range(n):
# print(ans)
print(ans)