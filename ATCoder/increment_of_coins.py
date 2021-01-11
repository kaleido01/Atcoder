import sys
sys.setrecursionlimit(10**7) #再帰関数の呼び出し制限


a, b, c = map(int, input().split())

dp = [[[ -1 for _ in range(105)]for _ in range(105)] for _ in range(105)]


for i in range(101):
  for j in range(101):
    for k in range(101):
      if i== 100 or j==100 or k ==100:
        dp[i][j][k] = 0


def f(x,y,z):
  res = 0
  if dp[x][y][z] >= 0:
    return dp[x][y][z]
  n = x+y+z
  res += (x/n)* f(x+1,y,z)
  res += (y/n)* f(x,y+1,z)
  res += (z/n)* f(x,y,z+1)
  res += 1
  dp[x][y][z] = res
    
  return res
    
    
print(f(a,b,c))

    
