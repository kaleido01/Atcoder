import math
a, b = list(input().split())

b = b.replace(".","")


# if a > 10**8:
#   a /= 10**8
#   print(a, b)
#   ans = a * b
#   print(a* b)
#   print(int(ans * (10 ** 8) //100))
# else:
ans = int(a) * int(b)
# print(ans)
print(int(ans//100))

