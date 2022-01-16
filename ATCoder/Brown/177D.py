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

n, m = mapInt()

grid = [ [] for i in range(n)]

for i in range(m):
  a, b = listInt()
  a -= 1
  b -= 1
  
  grid[a].append(b)
  grid[b].append(a)
  
from collections import defaultdict
class UnionFind:
    # 参考 https://note.nkmk.me/python-union-find/
    def __init__(self, n):
        self.n = n
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

    def size(self, x):       # 木のサイズ(グループ内に何人いるか、何個あるか)
        return -self.parents[self.root(x)]

    def same(self, x, y):    # 同じ木に属するか
        return self.root(x) == self.root(y)

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):   # グループ数
        return len(self.roots())
    
    # 要素xが属するグループに属する要素をリストで返す
    def members(self, x):
        root = self.root(x)
        return [i for i in range(self.n) if self.find(i) == root]
    
    # {ルート要素: [そのグループに含まれる要素のリスト], ...}のdefaultdictを返す
    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.root(member)].append(member)
        return group_members

    #ルート要素: [そのグループに含まれる要素のリスト]を文字列で返す
    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())



uf = UnionFind(n)

for i in range(n):
  for node in grid[i]:
    # print(i, node)
    uf.union(i, node)
    

# print(uf.roots())
ans = 0
# for members in uf.all_group_members().items():
#   # print(members)
#   ans = max(ans, len(members[1]))
for i in range(n):
  ans = max(ans, uf.size(i))

print(ans)

