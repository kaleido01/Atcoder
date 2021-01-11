import math

v,e= map(int, input().split())

# nodes = [[] for _ in range(v)] 
# weight = [[ 0 for _ in range(v)] for _ in range(v)]
dp = [[math.inf for  _ in range(v)] for i in range(v)]
for i in range(e):
  s,t,d = map(int, input().split())
  s -=1
  t -=1
  dp[s][t] = d
  dp[t][s] = d
  



for i in range(v):
    dp[i][i]=0

for k in range(v):
  for i in range(v):
    for j in range(v):
      dp [i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
      
# print(dp)
ans = [0] *v
for i in range(v):
  for j in range(v):
    ans[i] = max(ans[i], dp[i][j])
    
print(min(ans))