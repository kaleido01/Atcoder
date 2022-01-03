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
seg = SegmentTree(max, -INF, W)  # 区間最大値取得
#seg = SegmentTree(min, INF, W)  # 区間最小値取得
#seg = SegmentTree(add, 0, W)  # 区間和取得

# dp = [-INF] * (W + 1)
# dp[0] = 0
# seg.set(0, 0)

# for L, R, V in S:
#     for w in range(L, R):
#         dp[w] = max(dp[w], seg.prod(0, w - L + 1) + V)
#     for w in range(R, W + 1):
#         dp[w] = max(dp[w], seg.prod(w - R, w - L + 1) + V)
#     seg = SegmentTree(max, -INF, dp)

# print(dp[W] if dp[W] > 0 else -1)