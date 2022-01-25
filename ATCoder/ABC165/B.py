import math
import sys
n = int(input())

count = 0

s = 100
while(True):
  count += 1
  x = list(str(s))
  x = x[:len(x)-2]
  # print(x)
  # print(int("".join(x)))
  s += int("".join(x))
  if s >= n:
    print(count)
    sys.exit()
  