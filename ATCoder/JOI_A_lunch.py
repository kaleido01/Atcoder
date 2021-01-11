a = [int(input()) for _ in range(3)]
b = [int(input()) for _ in range(2)]

ans = 10000

for v1 in a:
  for v2 in b:
    ans = min(ans, v1 + v2 - 50)
    
print(ans)