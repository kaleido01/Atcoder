import sys
sys.setrecursionlimit(10 ** 8)


def rec(s,e):
    if dp[s][e] >= 0:
      return dp[s][e]
  
    if abs(s-e) <= 1:
      return 0
    
    res = 0
    if abs(w[s+1]-w[e-1]) <= 1 and rec(s+1,e-1) == e-s-2:
      # dp[s][e] = max(dp[s][e], dp[s+1][e-1] + 2)
      res = e - s
    
    for mid in range(s+1,e-1):
      left = rec(s,mid)
      right = rec(mid, e)
      res = max(res, left + right)
    
    dp[s][e] = res
    return dp[s][e]
  
while(True):
  n = int(input())
  if n == 0:
    break
  
  w = list(map(int, input().split()))
  dp = [[ -1 for _ in range (n)] for _ in range (n)]
  
  ans = rec(0,n-1)
  print(ans)