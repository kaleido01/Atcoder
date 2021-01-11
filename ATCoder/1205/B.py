import math
from functools import reduce
n = int(input())
s = input()

# allS = "101" * 10**10

def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)


num = s.count("101")
start = s.find("101")

if num * 3 == n:
  print(3 * (10**10) - num + 1)
else:
  minimum = "101" * 3*n
  c = minimum.count(s)
  print(c)
  first = (10 ** 10 // 3*n) * c
  amari = (10 ** 10 // 3*n) % c
  last = "101" * amari
  first += last.count(s)
  print(first)

  
  
ans = ("101" * 3).count("1011")
print(ans)