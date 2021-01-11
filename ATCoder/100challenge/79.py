n, m, q = map(int, input().split())

x = [[ 0 for i in range(n+5)]for i in range(n+5)]
c = [[ 0 for i in range(n+5)]for i in range(n+5)]

for i in range(m):
  l,r = map(int, input().split())
  x[l][r] += 1
  
for i in range(n+5):
  for j in range(1,n+5):
    c[i][j] =c[i][j-1] + x[i][j]
    

for i in range(q):
  ans = 0
  pi, qi = map(int, input().split())
  for j in range(pi, qi+1):
    ans +=c[j][qi]
  print(ans)
    
    
