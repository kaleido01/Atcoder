# -*- coding: utf-8 -*-
from socket import inet_aton
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
from operator import itemgetter, truediv
from collections import defaultdict
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
    
    # 要素xが属するグループに属する要素をリストで返す
    def members(self, x):
        root = self.root(x)
        return [i for i in range(self.n) if self.root(i) == root]
    
    # {ルート要素: [そのグループに含まれる要素のリスト], ...}のdefaultdictを返す
    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.root(member)].append(member)
        return group_members

    #ルート要素: [そのグループに含まれる要素のリスト]を文字列で返す
    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())





n, m = mapInt()
done = [False] * (n)
done2 = [False] * (n)
dic = {}
grid = [ [] for i in range(n)]
gridR = [ [] for i in range(n)]
# その頂点に向かっている辺の数（入力辺の数)
in_edge = [0] * n

uf = UnionFind(n)
for i in range(m):
  a, b = mapInt()
  a -= 1
  b -= 1
  if (a, b) in dic:
    continue
  dic[(a, b)] = True
  grid[a].append(b)
  gridR[b].append(a)
  in_edge[b] += 1
  # if uf.same(a, b):
  #   print(-1)
  #   sys.exit()
  # uf.union(a,b)





minHeap = []
for i in range(n):
  if in_edge[i] == 0:
    heapq.heappush(minHeap, i)

if len(minHeap) == 0:
  print(-1)
  sys.exit()
#startから追っていく
ans = []
# print(in_edge)
while(minHeap):
  x = heapq.heappop(minHeap)
  ans.append(x+1)
  for node in grid[x]:
    in_edge[node] -= 1
    if in_edge[node] == 0:
      heapq.heappush(minHeap, node)


if len(ans) != n:
  print(-1)
  sys.exit()
print(*ans)