n =int(input())


ans =0
for i in range(n):
  s,e = map(int, input().split())
  ans += e *(e+1)//2 - (s-1) *s//2
  
print(ans)