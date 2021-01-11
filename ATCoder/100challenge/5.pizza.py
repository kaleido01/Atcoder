a, b, c, x, y = map(int, input().split())

money = float("INF")
# for i in range(x+1):
#   for j in range(y+1):
#     res = max(x-i, y-j)*2
#     money = min(money, i*a+j*b+res*c)
# print(money)

n = max(x, y)
for i in range(0, 2*(n+2), 2):
    resx = max(0, x - i//2)
    resy = max(0, y - i//2)
    money = min(money, resx*a+resy*b+i*c)
print(money)