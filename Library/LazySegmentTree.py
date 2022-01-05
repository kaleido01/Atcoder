INF = 10 ** 9




#区間操作を変更する場合は init時のnodeを埋める場所のmin, 
class LazySegmentTree:
  n = 1
  node = []
  nodeInit = INF
  lazy = []
  def __init__(self, array, nodeInit):
    size = len(array)
    self.nodeInit = nodeInit
    
    while(self.n < size):
      self.n *= 2
    
    
    self.node = [nodeInit for _ in range(2*self.n - 1)]
    
    # この初期値はこの値であれば更新する必要がないものとして扱われる。
    self.lazy = [0 for _ in range(2*self.n - 1)]
    
    #最下段に値を入れたあとに、下の段から順番に値を入れる
    for i in range(size):
      self.node[i+self.n-1] = array[i]
        
    #値を入れるには、自分の子の 2 値を参照すれば良い　
    for i in range(self.n-2,-1, -1):
      self.node[i] = min(self.node[2*i+1],self.node[2*i+2])

  
  # 例で書かれているのは区間更新ではなく区間加算、区間更新を行う場合、遅延配列のフラグが立っているかをのbool配列を別で用意する必要がある。
  def eval(self, k, l, r):
    #値が無ければ何もしない
    if self.lazy[k] == 0: return
    
    self.node[k] += self.lazy[k]
    #最下段でないことを確認して、子ノードに値を伝搬
    print(k, self.node, self.lazy)
    if r - l > 1:
      self.lazy[2*k + 1] += self.lazy[k]/2
      self.lazy[2*k + 2] += self.lazy[k]/2
    
    #最後に遅延配列の値を戻す
    self.lazy[k] = 0
    
  def add(self, a, b, x, k = 0, l = 0, r = -1):
    if (r < 0): r = self.n
    
    #k番目のノードに対して遅延評価を行う
    self.eval(k, l, r)
    
    if b <= l or r <= a: return
    
    #完全被覆している場合、遅延配列を入れた後に評価
    if a <= l and r <= b:
      self.lazy[k] += (r-l) * x
      self.eval(k, l, x)
    
    else:
      self.add(a, b, x, 2*k+1, l, (l+r) // 2)
      self.add(a, b, x, 2*k+2, (l+r) // 2, r)
      self.node[k] = self.node[2*k+1] + self.node[2*k+2]
      
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

      self.eval(k, l, r);
      # 要求区間が対象区間を完全に被覆 -> 対象区間を答えの計算に使う
      if a <= l and r <= b:
        return self.node[k]

      # 要求区間が対象区間の一部を被覆 -> 子について探索を行う
      #左側の子を vl ・ 右側の子を vr としている
      # 新しい対象区間は、現在の対象区間を半分に割ったもの
      vl = self.getmin(a, b, 2*k+1, l, (l+r)/2)
      vr = self.getmin(a, b, 2*k+2, (l+r)/2, r)
      return min(vl, vr)


a = [1,2,3,4,5,6,7,8]
tree = LazySegmentTree(a, INF)


tree.add(0, 5, 7)
print(tree.node, tree.lazy)