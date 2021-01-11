import math
from functools import reduce
n, m = map(int, input().split())

a = list(map(int, input().split()))


def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)


l = lcm_list(a)


if m- l // 2<0:
  print(0)
else:
  print( (m-l//2) // l +1)