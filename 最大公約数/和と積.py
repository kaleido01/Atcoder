import math
a, b = map(int, input().split())


# g = math.gcd(a, b)

# a //= g
# b //= g

# print(g * math.gcd(a + b, g))



print(math.gcd(a+b, a * b))