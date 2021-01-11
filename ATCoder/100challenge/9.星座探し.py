m = int(input())


x = [0] * m
y = [0] * m

for i in range(m):
  x[i],y[i] = map(int, input().split())

n = int(input())

a = [0]* n
b = [0] * n
for i in range(n):
  a[i],b[i] = map(int, input().split())

match = 0
p1,p2 = x[0],y[0]
for i in range(n):
  dx,dy= a[i]-p1, b[i]-p2
  for j in range(m):
    for k in range(n):
      if a[k] == x[j]+dx and b[k] == y[j] + dy:
        match +=1
  if match == m:
    print(dx, dy)
    break
  match = 0
    
        