import math
import sys
n, x = map(int, input().split())

l = list(map(int, input().split()))


maxD=math.inf
if n == 1:
  print(abs(l[0]-x))
  sys.exit()
for i in range(n-1):
  a = abs(l[i] - x )
  b = abs(l[i+1] - x )
  maxD = min(maxD, math.gcd(a,b))
  
print(maxD)