import math
n = int(input())

a = list(map(int, input().split()))


ans = 0
# for i in range(n-1):
#   cost = math.inf
#   index = 0
#   for j in range(len(a)-1):
#     if (cost > a[j] + a[j+1]):
#       cost =  a[j] + a[j+1]
#       index = j
#   ans += cost
#   # print(index, cost)
#   a.pop(index)
#   a.pop(index)
#   a.insert(index, cost)
#   # print(a)
# print(ans)

dp = [[math.inf for _ in range(n)] for _ in range(n)]

def rec(l, r):
  if dp[l][r] != math.inf:
    return dp[l][r]
  if r-l == 0:
    return 0
  if r-l==1:
    dp[l][r] = a[l] + a[r]
    return a[l] + a[r]
  
  cost = math.inf
  for mid in range(l+1,r):
    cost = min(cost, rec(l,mid) + rec(mid,r))
  dp[l][r] = cost
  return cost

print(rec(0,n-1))
print(dp)