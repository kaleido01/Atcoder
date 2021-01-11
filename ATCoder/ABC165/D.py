import math

A, B, N = map(int, input().split())


x = min(B-1, N)
ans = math.floor(A*x / B)

print(ans)