n ,k = map(int, input().split())

a = list(map(int, input().split()))
f = list(map(int, input().split()))


a.sort()
f.sort(reverse = True)

def isOk(key):
  m=0
  for j in range(n):
    m += max(a[j] - key//f[j],0)
  return m <= k

def binary_search():
  left = -1
  right = 10**12
  
  while(right - left >1):

    middle = (left + right)//2
    if isOk(middle):
      right = middle
    else:
      left = middle
  return right

print(binary_search())
# print(ans)


