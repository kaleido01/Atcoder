import sys
n,m,t = map(int, input().split())

maxn = n
a =[0] * m
b = [0] * m

for i in range(m):
  x,y = map(int, input().split())
  a[i] = x
  b[i] = y
  
  


for i in range(m):
  if i==0:
    n -= a[i]
  else:
    n -= a[i] - b[i-1]
  if n<=0:
    print("No")
    sys.exit()
  if n + b[i] - a[i]>=maxn:
    n = maxn
  else:
    n += b[i] - a[i]

  
lastTime = b[-1]

n -= t-lastTime

if n <=0:
  print("No")
else:
  print("Yes")
    
    