n = int(input())

an = list(map(int, input().split()))


a = an[0]
b = an[1]
s = a + b

x = 0
for i in range(2,n):
  x ^= an[i]


dp = [[[-1,-1],[-1,-1]] for i in range(50)]
dp[0][0][0] = 0

v = 1
for i in range(49):
  cx = x & 1
  cs = s & 1
  ca = a & 1
  for j in range(2):
    for k in range(2):
      if dp[i][j][k] == -1: continue
      for na in range(2):
        for nb in range(2):
          ni = i+1
          nj, nk = 0, k
          if na ^ nb != cx : continue
          ns = na+nb+j
          if ns % 2 != cs : continue
          
          if ns>=2: nj = 1
          
          if na > ca : nk = 1
          elif na == ca : nk = k
          else: nk = 0
          
          dp[ni][nj][nk] = max(dp[ni][nj][nk], dp[i][j][k] | (na*v))
          
  x >>= 1
  s >>= 1
  a >>= 1
  v <<= 1
    
# print(an[0],dp[0:10])
if dp[49][0][0] == -1 or dp[49][0][0] == 0:
  print(-1)
else:
  print(an[0] - dp[49][0][0])