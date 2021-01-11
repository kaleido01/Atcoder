a, b, k = map(int, input().split())


if a - k>=0:
  print(a-k, b)
elif a+b - k>=0:
  print(0, a+b-k)
else:
  print(0,0)