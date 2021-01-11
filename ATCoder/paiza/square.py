import math

max_n = 100000

n=int(input())

query = [ [ (-1,-1) for i in range(2* max_n)] for i in range(n)]
plus = [False] * n

for i in range (n):
  o, x, y, a = list(input().split())
  x = int(x)
  y = int(y)
  a = int(a)
  if o == "+":
    plus[i] = True
    #y方向に各回での演算内容を描いていく
  for j in range(y, y + a):
    query[i][j]=(x,a)
    


# print("plus" , plus)
# print("query" , query)

sz = max_n*2
u = 1
while(u < sz):
  u *= 2


#最下段に値を入れたあとに、下の段から順番に値を入れる
# for i in range(sz):
#   node[i+n-1] = v[i]
    
#値を入れるには、自分の子の 2 値を参照すれば良い
# for i in range(n-2,-1, -1):
#   node[i] = min(node[2*i+1],node[2*i+2])



def update(x:int, val:int):
    #最下段のノードにアクセスする
    x += (u - 1)
    #最下段のノードを更新したら、あとは親に上って更新していく
    node[x] = val
    while(x > 0):
      x = (x - 1) // 2;
      node[x] = node[2*x+1] + node[2*x+2]
    


## 要求区間 [a, b) 中の要素の最小値を答える
## k := 自分がいるノードのインデックス
## 対象区間は [l, r) にあたる
def getmin(a:int, b:int, k=0, l=0, r=-1):
    #最初に呼び出されたときの対象区間は [0, n)
    if(r < 0):
      r = u

    #要求区間と対象区間が交わらない -> 適当に返す
    if r <= a or b <= l:
      return 0

    # 要求区間が対象区間を完全に被覆 -> 対象区間を答えの計算に使う
    if a <= l and r <= b:
      return node[k]

    # 要求区間が対象区間の一部を被覆 -> 子について探索を行う
    #左側の子を vl ・ 右側の子を vr としている
    # 新しい対象区間は、現在の対象区間を半分に割ったもの
    vl = getmin(a, b, 2*k+1, l, (l+r)/2)
    vr = getmin(a, b, 2*k+2, (l+r)/2, r)
    return vl + vr


ans = 0
node = [0 for _ in range(2*u-1)]
for j in range(2*max_n):
  
  for i in range(n):
    
    x, a = query[i][j]
    
    if x == a == -1:
      continue
    for k in range(x, x + a):
      if plus[i]:
        update(k,1)
      else:
        update(k,0)
    
  # print(getmin(0, max_n))
  # print(node)
  ans += getmin(0, max_n)
    
print(ans)