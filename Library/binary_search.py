

a=[1,2,3,4,5,6,7,8,9,10101]
# def binary_search(value):
#   left = 0
#   right = len(a)-1
  
#   while(left<= right):
#     middle = (left + right) // 2
#     if value < a[middle]:
#       right = middle - 1
#     elif value > a[middle]:
#       left = middle + 1
#     else:
#       return middle
#   return -1
  
# print(binary_search(1))


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
      