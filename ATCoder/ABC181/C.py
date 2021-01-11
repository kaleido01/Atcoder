from itertools import combinations
import sys
n = int(input())

l=[]
for _ in range(n):
  x,y = map(int, input().split())
  l.append((x,y))

c = combinations(l, 3)


for v in c:
  # 傾き計算ができない時
  if v[0][0] == v[1][0] and  v[1][0] == v[2][0]:
    print("Yes")
    sys.exit()
  if v[0][0] == v[1][0] or v[1][0] == v[2][0]:
    continue

  # alpha1 = (v[1][1] - v[0][1]) / (v[1][0] - v[0][0])
  # beta1 = (-1) * alpha1 * v[0][0] + v[0][1]
  
  # print(alpha1, beta1)
  
  # alpha2 = (v[2][1] - v[1][1]) / (v[2][0] - v[1][0])
  # beta2 = (-1) * alpha2 * v[1][0] + v[1][1]
  
  left = (v[1][0] - v[0][0]) * (v[2][1] - v[0][1])
  right =  (v[2][0] - v[0][0]) * (v[1][1] - v[0][1])
  
  if left == right:
    print("Yes")
    sys.exit()

print("No")