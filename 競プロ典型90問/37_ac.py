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



# h, w = mapInt()
w, n = mapInt()

g = []

for i in range(n):
  g.append(listInt())
  
dp = inithwv(n+1,w+1,0)
v = [-1] * (w+1)
tree = segmentTree(v)

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