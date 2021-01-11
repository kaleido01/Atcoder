import math
from functools import reduce
n = int(input())



x = []
for i in range(2,n+1):
  x.append(i)
  


def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)


print(lcm_list(x)+1)

# 27