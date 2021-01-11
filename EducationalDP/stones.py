n, k = map(int,input().split())

a = list(map(int, input().split()))

dp = [False] * (k+1)

for i in range(k):
  for j in range(n):
    if i+1-a[j] < 0:
      continue
    if dp[i+1-a[j]] == False:
      dp[i+1] = True
print(dp)
if dp[k] == False:
  print("Second")
else:
  print("First")