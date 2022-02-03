# -*- coding: utf-8 -*-
import sys
import heapq
import math

sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
mapInt = lambda: map(int, input().split())
listInt = lambda: list(map(int, input().split()))

init0 = lambda n: [0 for _ in range(n)]
inithwv = lambda h, w, v: [[v for _ in range(w)] for _ in range(h)]
inithw = lambda h, w, v: [ listInt() for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]

YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1
from operator import itemgetter

# en = 50
en = 2 * 10**5
n, q = mapInt()

infant = [0 for i in range(n)]
world = [[] for i in range(en)]
deleteWorld = [[] for i in range(en)]

maxInfant = [INF for i in range(en)]

for i in range(n):
  a, b = mapInt()
  b -= 1
  infant[i] = [b,a]
  heapq.heappush(world[b],-1 * a)
  
# print(infant)

for i in range(en):
  if len(world[i]) == 0:
    continue
  # v = heapq.heappop(world[i])
  maxInfant[i] = -1 * world[i][0]
  

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



# print(maxInfant)
seg = segmentTree(maxInfant)
# print(maxInfant)
for i in range(q):
  c, d = mapInt()
  c -= 1
  d -= 1
  place, value = infant[c]
  # print(value)
  heapq.heappush(deleteWorld[place],-1 * value)
  heapq.heappush(world[d],-1 * value)
  infant[c][0] = d
  
  # 影響を及ぼすのはc園とd園のふたつ
  # c園の更新
  # print(world[place][0],deleteWorld[place][0])
  while(world[place][0] == deleteWorld[place][0]):
    heapq.heappop(world[place])
    heapq.heappop(deleteWorld[place])
    
    if len(deleteWorld[place]) == 0:
      break
  # print(place)
  if len(world[place])!=0:
    seg.update(place,-1 * world[place][0])
  else:
    seg.update(place,INF)
    
  seg.update(d,-1 * world[d][0])
  # print(deleteWorld[place][0])
  # print(world[d][0])
  # print(seg.node[0:80])
    

  print(seg.getmin(0, en))
  
  

  