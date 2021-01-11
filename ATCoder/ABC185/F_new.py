n,q = map(int, input().split())
A = list(map(int, input().split()))


#seg tree 準備
sz = len(A)
n = 1
while(n < sz):
  n *= 2
node = [0 for _ in range(2*n-1)]

#最下段に値を入れたあとに、下の段から順番に値を入れる
for i in range(sz):
  node[i+n-1] = A[i]
    
#値を入れるには、自分の子の 2 値を参照すれば良い
for i in range(n-2,-1, -1):
  node[i] =node[2*i+1] ^ node[2*i+2] 


# print(node)


def update(x:int, val:int):
  #最下段のノードにアクセスする
  x += (n - 1)
  #最下段のノードを更新したら、あとは親に上って更新していく
  node[x] = val
  while(x > 0):
    x = (x - 1) // 2
    node[x] = node[2*x+1] ^ node[2*x+2]

      
# 要求区間 [a, b) 中の合計値を答える
## k := 自分がいるノードのインデックス
## 対象区間は [l, r) にあたる
def getXor(a:int, b:int, k=0, l=0, r=-1):
    #最初に呼び出されたときの対象区間は [0, n)
    if(r < 0):
      r = n

    #要求区間と対象区間が交わらない -> 適当に返す
    if r <= a or b <= l:
      return 0

    # 要求区間が対象区間を完全に被覆 -> 対象区間を答えの計算に使う
    if a <= l and r <= b:
      return node[k]

    # 要求区間が対象区間の一部を被覆 -> 子について探索を行う
    #左側の子を vl ・ 右側の子を vr としている
    # 新しい対象区間は、現在の対象区間を半分に割ったもの
    vl = getXor(a, b, 2*k+1, l, (l+r)//2)
    vr = getXor(a, b, 2*k+2, (l+r)//2, r)
    
    return vl ^ vr

for i in range(q):
  t, x, y = map(int, input().split())
  if t==1:
    update(x-1,A[x-1] ^ y)
    A[x-1] = A[x-1] ^ y
  else:
    print(getXor(x-1, y))