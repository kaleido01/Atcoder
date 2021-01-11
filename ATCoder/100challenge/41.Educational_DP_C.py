n = int(input())


a = [ [0,0,0] for _ in range(n)]

for i in range(n):
  x,y,z = map(int, input().split())
  a[i][0],a[i][1],a[i][2]= x,y,z

  
dp = [[0,0,0] for _ in range(n+1)]

for i in range(n):
  for j in range(3):
    for k in range(3):
      if j == k:
        continue
      dp[i+1][j]= max(dp[i+1][j], dp[i][k] + a[i][k])
      
      
print(max(dp[n]))