n = int(input())

for i in range(n):
  x = list(input())
  y = list(input())
  
  dp = [[0] * (len(y)+1) for _ in range(len(x)+1)]
  
  for j in range(len(x)):
    for k in range(len(y)):
      if x[j] == y[k]:
        dp[j+1][k+1] =dp[j][k] +1
      else:
        dp[j+1][k+1] = max(dp[j+1][k], dp[j][k+1])
        
  print(dp[j+1][k+1])