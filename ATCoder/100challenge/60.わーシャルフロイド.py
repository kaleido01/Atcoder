import math

v,e= map(int, input().split())

# nodes = [[] for _ in range(v)] 
# weight = [[ 0 for _ in range(v)] for _ in range(v)]
dp = [[math.inf for  _ in range(v)] for i in range(v)]
for i in range(e):
  s,t,d = map(int, input().split())
  # s -=1
  # t -=1
  dp[s][t] = d
  



for i in range(v):
    dp[i][i]=0

for k in range(v):
  for i in range(v):
    for j in range(v):
      dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
      
    
isNegative = False
for i in range(v):
  if dp[i][i] <0:
    print("NEGATIVE CYCLE")
    isNegative = True
    break
  
if not isNegative:
  # for i in range(v):
  #   for j in range(v):
  #     if dp[i][j] == math.inf:
  #       print("INF", end="")
  #     else:
  #       print(dp[i][j], end ="")
  #     if j != v-1:
  #       print(" ",end ="")
  #   if i != v-1:
  #     print()
  for v in dp:
      print(*[str(e).upper() for e in v])