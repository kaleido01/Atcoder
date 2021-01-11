n = int(input())




s = ""
while(n >= 0):
  m = n % 36
  if 0 <= m <= 9:
    s += str(m)
  else:
    s += chr(65 + m - 10)
  
  n //= 36
  if n ==0:
    break
  
print(s[::-1])