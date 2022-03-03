# -*- coding: utf-8 -*-
from re import S
import sys, getpass, string
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
INF=10**18
MOD=10**9+7 # 998244353
sys.setrecursionlimit(10**5)

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
# https://github.com/tatyam-prime/SortedSet/blob/main/SortedMultiset.py
import math
from bisect import bisect_left, bisect_right, insort
from typing import Generic, Iterable, Iterator, Set, TypeVar, Union, List
class segmentTree:
  
  n = 1
  node =[]
  def __init__(self, array):
    size = len(array)
    while(self.n < size):
      self.n *= 2
    
    self.node = [INF for _ in range(2*self.n-1)]
    
    #最下段に値を入れたあとに、下の段から順番に値を入れる
    for i in range(size):
      self.node[i+self.n-1] = array[i]
        
    #値を入れるには、自分の子の 2 値を参照すれば良い
    for i in range(self.n-2,-1, -1):
      self.node[i] = min(self.node[2*i+1],self.node[2*i+2])

  def update(self, x:int, val:int):
      #最下段のノードにアクセスする
      x += (self.n - 1)
      #最下段のノードを更新したら、あとは親に上って更新していく
      self.node[x] = val
      while(x > 0):
        x = (x - 1) // 2;
        self.node[x] = min(self.node[2*x+1], self.node[2*x+2])
    


  ## 要求区間 [a, b) 中の要素の最小値を答える
  ## k := 自分がいるノードのインデックス
  ## 対象区間は [l, r) にあたる
  def getmin(self, a:int, b:int, k=0, l=0, r=-1):
      #最初に呼び出されたときの対象区間は [0, n)
      if(r < 0):
        r = self.n

      #要求区間と対象区間が交わらない -> 適当に返す
      if r <= a or b <= l:
        return INF

      # 要求区間が対象区間を完全に被覆 -> 対象区間を答えの計算に使う
      if a <= l and r <= b:
        return self.node[k]

      # 要求区間が対象区間の一部を被覆 -> 子について探索を行う
      #左側の子を vl ・ 右側の子を vr としている
      # 新しい対象区間は、現在の対象区間を半分に割ったもの
      vl = self.getmin(a, b, 2*k+1, l, (l+r)/2)
      vr = self.getmin(a, b, 2*k+2, (l+r)/2, r)
      return min(vl, vr)

  ## 要求区間 [a, b) 中の要素の最大値を答える
  ## k := 自分がいるノードのインデックス
  ## 対象区間は [l, r) にあたる
  def getmax(self, a:int, b:int, k=0, l=0, r=-1):
      #最初に呼び出されたときの対象区間は [0, n)
      if(r < 0):
        r = self.n

      #要求区間と対象区間が交わらない -> 適当に返す
      if r <= a or b <= l:
        return -1 * INF

      # 要求区間が対象区間を完全に被覆 -> 対象区間を答えの計算に使う
      if a <= l and r <= b:
        return self.node[k]

      # 要求区間が対象区間の一部を被覆 -> 子について探索を行う
      #左側の子を vl ・ 右側の子を vr としている
      # 新しい対象区間は、現在の対象区間を半分に割ったもの
      vl = self.getmax(a, b, 2*k+1, l, (l+r)/2)
      vr = self.getmax(a, b, 2*k+2, (l+r)/2, r)
      return max(vl, vr)
    
    
    
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

INF = 10 ** 16
from operator import add

Q = int(input())
q = []
# 座標圧縮したい数列
t = []
for i in range(Q):
  x = listInt()
  t.append(x[1])
  q.append(x)



# 集合型にすることで重複を除去し、
# 小さい順にソートする
B = sorted(set(t))

# B の各要素が何番目の要素なのかを辞書型で管理する
D = { v: i for i, v in enumerate(B) }

# 答え
x = list(map(lambda v: D[v], t))

ans = []

def isOk(l,r, key):
  """不等号を入れ替える場合は呼び出し側のOKとNGのmiddleも入れ替える"""
  # return a[index] <= key
  print("key", key, seg.prod(l, r), l, r)
  return seg.prod(l, r) <= key


def binary_search(v, l, r):
    ok = r
    ng = l
    # ng = -1
    # ok = len(a)
    while(abs(ok-ng) > 1):
      middle = (ok + ng) // 2
      if isOk(ng, middle, v):
        ok = middle
      else:
        ng = middle
    return ok

print(t, list(x))
cnt = 0
seg = SegmentTree(add, 0, len(x))  # 区間和取得
for i in range(Q):
  if q[i][0] == 1:
    seg.set(x[cnt], seg.get(x[cnt])+1)
    # print(seg)
  elif q[i][0] == 2:
    index = binary_search(q[i][2],  x[cnt], -1)
    print(index)
    if index == -1:
      ans.append(-1)
    else:
      ans.append(t[index])
  else:
    # print(x)
    index = binary_search(q[i][2], x[cnt], len(t))
    print(index)
    if index == len(t):
      ans.append(-1)
    else:
      ans.append(t[index])
  cnt +=1


print(seg)
print(*ans)