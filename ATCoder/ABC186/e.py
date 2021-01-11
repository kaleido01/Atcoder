import math
n = int(input())

def extgcd(a, b):
    if b:
        d, y, x = extgcd(b, a % b)
        y -= (a // b)*x
        return d, x, y
    return a, 1, 0

for i in range(n):
  n, s, k = map(int, input().split())
  g = math.gcd(k,n)
  if s % g != 0:
    print(-1)
    continue
  k //= g
  n //= g
  s //= g
  
  g, x, y = extgcd(k,n)
  print(x * (-s) % n)


# n, s, k = map(int, input().split())
# g = math.gcd(k,n)

# k //= g
# n //= g


# print(g,x,y)
# print(g)