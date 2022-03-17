# -*- coding: utf-8 -*-
import sys, getpass, string
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
sys.setrecursionlimit(3*10**5+10)
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

    def size(self, x):       # 木のサイズ
        return -self.parents[self.root(x)]

    def same(self, x, y):    # 同じ木に属するか
        return self.root(x) == self.root(y)

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):   # グループ数
        return len(self.roots())
    
    # 要素xが属するグループに属する要素をリストで返す
    def members(self, x):
        r = self.root(x)
        return [i for i in range(self.n) if self.root(i) == r]
    
    # {ルート要素: [そのグループに含まれる要素のリスト], ...}のdefaultdictを返す
    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.root(member)].append(member)
        return group_members

    #ルート要素: [そのグループに含まれる要素のリスト]を文字列で返す
    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())



# n = int(input())
# s = input()
# h, w = mapInt()
v, e = mapInt()
pq = []
uf = UnionFind(v)


dp = [[math.inf for  _ in range(v)] for i in range(v)]
for i in range(e):
  s,t,d = map(int, input().split())
  s -=1
  t -=1
  dp[s][t] = d
  dp[t][s] = d
  heapq.heappush(pq, (d, s, t))
  
  
for i in range(v):
    dp[i][i] = 0

for k in range(v):
  for i in range(v):
    for j in range(v):
      dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
      


rest = []
dpA = [[math.inf for  _ in range(v)] for i in range(v)]

while pq:
  d, x, y = heapq.heappop(pq)
  if uf.same(x,y):
    rest.append((d, x, y))
  else:
    uf.union(x,y)
    dpA[x][y] = d
    dpA[y][x] = d
  
for i in range(v):
    dpA[i][i] = 0

for k in range(v):
  for i in range(v):
    for j in range(v):
      dpA[i][j] = min(dpA[i][j], dpA[i][k] + dpA[k][j])
ans = 0
# print(rest)
for i in range(len(rest)):
  d, x, y = rest[i]
  if dp[x][y] < d:
    ans +=1
  if dp[x][y] == d and dpA[x][y] == d:
    ans +=1
    

# print(dp)
# print(dpA)
print(ans)