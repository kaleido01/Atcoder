import math 

h,w,m = map(int, input().split())


minXZero = w-1
minYZero = h-1

# y軸からみて最初にある障害物
noStoneX = [h] * w

# x軸からみて最初にある障害物
noStoneY = [w] * h

# 各行に存在するobjectの位置
ends = [[] for i in range(h+1)]

for i in range(m):
  y,x = map(int, input().split())
  x -=1
  y -=1
  noStoneX[x] = min(noStoneX[x], y)
  noStoneY[y] = min(noStoneY[y], x)
  ends[y].append(x)
  if y == 0:
    minXZero = min(minXZero,x)
  if x == 0:
    minYZero = min(minYZero,y)
  
sumA = 0
sumB = 0

# print("minXZero", minXZero)
# print("minYZero", minYZero)
# print("noStoneX", noStoneX)
# print("noStoneY", noStoneY)
# print("ends", ends)

#縦方向の総和
for i in range(minXZero+1):
  sumA += noStoneX[i]
  
#縦方向の総和
for i in range(minYZero+1):
  sumB += noStoneY[i]
  

#segment-treeを使って縦方向へ重複している部分を足していく
length = minXZero + 1
n = 1
while(n < length):
  n *= 2

node = [0 for _ in range(2*n-1)]

#最下段に値を入れたあとに、下の段から順番に値を入れる
for i in range(length):
  node[i+n-1] = 1
    
#値を入れるには、自分の子の 2 値を参照すれば良い
for i in range(n-2,-1, -1):
  node[i] = node[2*i+1] + node[2*i+2]


def update(x:int, val:int):
    #最下段のノードにアクセスする
    x += (n - 1)
    #最下段のノードを更新したら、あとは親に上って更新していく
    node[x] = val
    while(x > 0):
      x = (x - 1) // 2;
      node[x] = node[2*x+1] + node[2*x+2]
    

## 要求区間 [a, b) 中の要素の最小値を答える
## k := 自分がいるノードのインデックス
## 対象区間は [l, r) にあたる
def getsum(a:int, b:int, k=0, l=0, r=-1):
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
    vl = getsum(a, b, 2*k+1, l, (l+r)/2)
    vr = getsum(a, b, 2*k+2, (l+r)/2, r)
    return vl + vr 
  
sumAB = 0

for y in range(minYZero + 1):

  for x in ends[y]:
    if x > minXZero:
      continue
    update(x,0)

  sumAB += getsum(0,noStoneY[y])
  

# print(sumA, sumB, sumAB)
print(sumA + sumB - sumAB)
