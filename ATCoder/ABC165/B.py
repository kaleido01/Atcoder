import math
import sys
n = int(input())

count = 0

s = 100
while(True):
  count +=1
  s += math.floor(s*0.01)
  if s>=n:
    print(count)
    sys.exit()
  