n, m = map(int, input().split())

a = [ int(input()) for _ in range(n)]

m1 = [0]

for i in range(len(a)):
  for j in range(i,len(a)):
    m1.append(a[i] + a[j])
    
m1.extend(a)

m1.sort()

def isOk(index, value):
  return m1[index] >= value

def lowerBound(value):
  ng = -1
  ok = len(m1)
  
  while((ok-ng)>1):
    middle = (ok + ng) //2
    
    if isOk(middle, value):
      ok = middle
    else:
      ng = middle
  return ok

ans = 0
for v in m1:
  upper = m-v
  
  if upper <=0:
    continue
  
  upperIndex = lowerBound(upper)

  if upperIndex<= 0:
    ans = max(ans, v)
  elif upperIndex == len(m1):
    ans = max(ans, v + m1[upperIndex-1])
  elif m1[upperIndex] == upper:
    ans = upper
  else:
    ans = max(ans, v + m1[upperIndex -1])
    

print(ans)