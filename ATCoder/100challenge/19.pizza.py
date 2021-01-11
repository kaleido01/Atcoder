d = int(input())
n = int (input())
m = int(input())

a = [ int(input()) for _ in range(n-1)]
orders = [int(input()) for _ in range(m)]
a.insert(0,0)
a.sort()
# print(a,orders)

def isOk(index, key):
  return a[index] >= key

def binary_search(v):
  left = -1
  right = len(a)
  
  while(right - left >1):
    # middle = left + (left - right)//2
    middle = (left + right)//2
    if isOk(middle, v):
      right = middle
    else:
      left = middle
  return right
      

sum = 0
for order in orders:
  shopIndex = binary_search(order)
  if shopIndex == len(a):
    sum += min(abs(a[shopIndex-1] -order), (d- order)+a[0])
  elif shopIndex == -1:
    sum += min(abs(a[0] -order), abs(a[-1] - d) +order)
  else:
    sum += min(abs(a[shopIndex]-order), abs(a[shopIndex-1] -order))
  
print(sum)