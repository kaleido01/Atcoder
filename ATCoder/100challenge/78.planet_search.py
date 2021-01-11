m,n = map(int, input().split())

query = int(input())

maze = [ list(input()) for _ in range(m)]

a=[[[0 for _ in range(3)]  for _ in range(n+1)] for _ in range(m+1)]

for i in range(m):
  for j in range(n):
    for k in range(2):
      if k == 0:
        if maze[i][j] == "J":
          a[i+1][j+1][k] = a[i+1][j][k] + a[i][j+1][k] - a[i][j][k] + 1
        else:
          a[i+1][j+1][k] = a[i+1][j][k] + a[i][j+1][k] - a[i][j][k]
      elif k ==1:
        if maze[i][j] == "O":
          a[i+1][j+1][k] = a[i+1][j][k] + a[i][j+1][k] - a[i][j][k] + 1
        else:
          a[i+1][j+1][k] = a[i+1][j][k] + a[i][j+1][k] - a[i][j][k]
      else:
        if maze[i][j] == "I":
          a[i+1][j+1][k] = a[i+1][j][k] + a[i][j+1][k] - a[i][j][k] + 1
        else:
          a[i+1][j+1][k] = a[i+1][j][k] + a[i][j+1][k] - a[i][j][k]

for _ in range(query):
  p, q, r, s=map(int, input().split())
  ans= [0] * 3
  for j in range(3):
      ans[j] = a[r][s][j] - a[p-1][s][j] - a[r][q-1][j] + a[p-1][q-1][j]
  print(ans[0],ans[1],ans[2])
  
