import math
from functools import reduce
import sys


def gcd_list(numbers):
    return reduce(math.gcd, numbers)
  

n,m = map(int, input().split())

l =[]
if m!=0:
  l = list(map(int, input().split()))

l.sort()
diff = [0] * (m+1)

if m == 0:
  print(1)
  sys.exit()
  
mindiff = math.inf
for i in range(len(l)):
  if i==0:
    diff[i] = l[i] -1
  else:
    diff[i] = l[i] - l[i-1] - 1
  if diff[i] != 0:
      mindiff = min(mindiff, diff[i])
  
diff[-1] = n - l[-1]
if diff[-1] != 0:
  mindiff = min(mindiff, diff[i])
    
    
ans = 0
for v in diff:
  if v !=0:
    if v % mindiff ==0:
      ans += v // mindiff
    else:
      ans += v //mindiff +1
# mingcd = gcd_list(diff)

# print(mindiff)
# print(diff)
print(ans)
