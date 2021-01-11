n,x,t = map(int, input().split())

ans = 0
if n % x == 0:
  ans = ((n//x)) * t
else:
  ans = ((n//x)+1) * t

print(ans)


