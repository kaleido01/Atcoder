n = int(input())
  
  
a = [-1] *60


def fibo(n):
  if a[n] >=0:
    return a[n]
  if n==0 or n == 1:
    return 0
  a[n] = fibo(n-1) + fibo(n-2)
  return fibo(n-1) + fibo(n-2)

a[0], a[1] = 1,1
ans = fibo(n)
print(ans)
1