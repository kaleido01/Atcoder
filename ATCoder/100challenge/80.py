import math

n = int(input())

S = [list(input()) for _ in range(5)]
# print(S)
dp=[[[False for i in range(5*n+10)] for _ in range(3)]for _ in range(n)]
# print(dp)
for i in range(n):
  R = 5
  B = 5
  W = 5
  for j in range(5):
    if S[j][i] == "R":
      R -= 1
    elif S[j][i] == "B":
      B -= 1  
    elif S[j][i] == "W":
      W -= 1
  if i == 0:
      dp[0][0][R] = True
      dp[0][1][W] = True
      dp[0][2][B] = True
      continue
  for j in range(5 * n +10):
    if dp[i-1][0][j]:
      dp[i][1][j+W] = True
      dp[i][2][j+B] = True
    if dp[i-1][1][j]:
      dp[i][2][j+B] = True
      dp[i][0][j+R] = True
    if dp[i-1][2][j]:
      dp[i][0][j+R] = True
      dp[i][1][j+W] = True

ans = math.inf
for j in range(3):
  for k in range(5 * n+5):
    if dp[n-1][j][k]:
      # print(k)
      ans = min(ans, k)
      break
      
# print(dp[1])
print(ans)