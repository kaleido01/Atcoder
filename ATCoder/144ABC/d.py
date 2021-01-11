import math

a, b, x  = map(int,input().split())


r = x / (a*a)
# print("r", r)

# 入っている水の面積
s = a* r

u = 2 * s / b
# v = 2 * s / a
# print("u",u)
if u <= a:
  f = math.sqrt(u * u + b * b)

  h = 2 * s / f
  # print(h, b,h/b)
  asin05 = math.asin(h/b)
  # print(asin05)
  print(90 - math.degrees(asin05))
else:
  top = 2 * s/a - b
  f = math.sqrt(a * a + (b-top) ** 2)
  p = math.asin(2*s / (f* (b + top)))
  # print(p)
  print(90- math.degrees(p))




