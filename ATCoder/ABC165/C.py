from itertools import combinations_with_replacement


n, m, q = map(int, input().split())

a =[0] * q
b =[0] * q
c =[0] * q
d =[0] * q

for i in range(q):
  x, y, z, zz = map(int, input().split())
  a[i] = x-1
  b[i] = y-1
  c[i] = z
  d[i] = zz
  

pattern =list(combinations_with_replacement([i for i in range(1,m+1)],n))

ans = 0
for A in pattern:
  sumd=0
  # print(A)
  for i in range(q):  
    bi = b[i]
    ai = a[i]
    ci = c[i]
    di = d[i]
    if A[bi] - A[ai] == ci:
      sumd += di
  ans = max(ans, sumd)

print(ans)