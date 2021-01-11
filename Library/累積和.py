
a = [1,2,3,4,5,6]

s = [0] * (len(a)+1)



for i in range(len(a)):
  s[i+1] = s[i] + a[i]
  
w = 6
h = 3
m = [[1,2,3,4,5,6], [2,3,4,5,6,7], [3,4,5,6,7,8]]

c = [[0 for _ in range(w+1)] for _ in range(h+1)]

for i in range(h):
  for j in range(w):
    c[i+1][j+1] = c[i+1][j] + c[i][j+1] - c[i][j] + m[i][j]


for sy in range(1,h+1):
  for sx in range(1,w+1):
    for ey in range(sy,h+1):
      for ex in range(sx,w+1):
        # 全体の長方形　- 縦の小さい長方形 - 横の小さい長方形 + 縦横小さい長方形 
        cost = c[ey][ex] - c[sy-1][ex] - c[ey][sx-1] + c[sy-1][sx-1]
        # print(cost)
print(c)

