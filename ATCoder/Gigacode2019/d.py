H,W,K,V = map(int, input().split())


field = [list(map(int,input().split())) for _ in range(H)]

c = [[0 for i in range(W+3)] for i in range(H+3)]

for i in range(1,H+1):
  for j in range(1,W+1):
    c[i][j] = c[i][j-1] + field[i-1][j-1]
    
for i in range(1,W+1):
  for j in range(1,H+1):
    c[j][i] = c[j][i] + c[j-1][i]

# print(c)
ans = 0
for sy in range(1,H+1):
  for sx in range(1,W+1):
    for ey in range(sy,H+1):
      for ex in range(sx,W+1):
        cost = c[ey][ex] - c[sy-1][ex] - c[ey][sx-1] + c[sy-1][sx-1] + K * (ey-sy +1) * (ex-sx+1)
        # print(cost)
        if V >= cost:
          ans = max(ans,  (ey-sy +1) * (ex-sx+1))
      
      
print(ans)