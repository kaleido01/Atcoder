n = int(input())

# ########関数部分##############
# def Base_10_to_n(X, n):
#     if (int(X/n)):
#         return Base_10_to_n(int(X/n), n)+str(X%n)
#     return str(X%n)
# ############################
 
 
 
# r = Base_10_to_n(n, 26)

# print(r)

ans = ""
# n -= 1
  
while(n > 0):
  
  # if 0 <= n <= 25:
  #   ans += chr(n + 97)
  #   break
  x = n % 26
  if x == 0:
    ans += chr(97 + 25)
    n //= 26
    n -= 1
  else:
    ans += chr(x-1 + 97)
    n //= 26
  
print(ans[::-1])