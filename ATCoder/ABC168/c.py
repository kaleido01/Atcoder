import math
a, b, h, m= map(int, input().split())

u = (h + m/60) / 12 * 360
v = m / 60 * 360

ta = math.radians(u)
tb = math.radians(v)

# print(u, v , ta, tb)

r = math.sqrt(a * a + b * b - 2* a * b *math.cos(tb - ta))

print(r)