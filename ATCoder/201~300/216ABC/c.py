import math
n = int(input())

ans = ""


while n != 0:
  if n % 2 == 0:
    ans += "B"
    n //= 2
  else:
    ans += "A"
    n -= 1

print(ans[::-1])


# a = []

# p = 1
# count = 0
# while(n != 0):
#   p *= 2
#   count += 1
#   if p < n:
#     count +=1
#   else:
#     a.append(count)
#     n -= p
#     count = 0
#     p = 1
    
    
