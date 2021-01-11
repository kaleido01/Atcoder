a, b, x, y = map(int, input().split())

if a > b:
  if a-b ==1:
    print(x)
  elif y >=2*x:
    print(2 * x * (a-b-1) + x)
  else:
    print(y * (a-b-1) + x)
else:
  if y >=2*x:
    print(2 * x * (b-a) + x)
  else:
    print(y * (b-a) + x)

# if a == b:
#     print(x)

# else:
#   if y >=2*x:
#     print(2 * x * abs(b-a) + x)
#   else:
#     print(y * abs(b-a) + x)
  
  
  