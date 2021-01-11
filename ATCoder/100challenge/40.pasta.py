n, k = map(int, input().split())

define = [-1] * 105

for i in range(k):
  p, q = map(int, input().split())
  define[p] = q

dp = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(n+2)]
if define[1] !=-1 and define[2] != -1:
  dp[3][define[2]][define[1]] = 1
elif define[1] !=-1:
  dp[3][1][define[1]] = 1
  dp[3][2][define[1]] = 1
  dp[3][3][define[1]] = 1
elif define[2] !=-1:
  dp[3][define[2]][1] = 1
  dp[3][define[2]][2] = 1
  dp[3][define[2]][3] = 1
else:
  for i in range (1,4):
    for j in range(1,4):
      dp[3][i][j] = 1



for i in range(3,n+1):
  # 当日が確定している場合
  if define[i] != -1:
    dDay = define[i]
    for j in range(1,4):
      for k in range(1,4):
        #当日のもの意外は0
        if  j != dDay:
          dp[i+1][j][k] = 0
        else:
          dp[i+1][j][k] += sum(dp[i][k]) % 10000
          #当日のもので前日と異なる場合
          if k == dDay:
            dp[i+1][j][k] -= dp[i][k][k]
    continue
  for j in range(1,4):
    for k in range(1,4):
      dp[i+1][j][k] = sum(dp[i][k]) % 10000
      if j == k:
       dp[i+1][j][j] -= dp[i][j][j]
      
print(sum(map(sum, dp[n+1]))% 10000)