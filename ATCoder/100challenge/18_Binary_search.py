n = int(input())
s = list(map(int, input().split()))

q = int(input())
t = list(map(int, input().split()))

def binary_search(v:int):
  left = 0
  right = n-1
  
  while(left<= right):
    middle = (left + right) // 2
    if v > s[middle]:
      left = middle + 1
    elif (v < s[middle]):
      right = middle -1
    else:
      return middle
  return -1

ans = 0
for v in t:
  if not binary_search(v) == -1:
    ans +=1

print(ans)

