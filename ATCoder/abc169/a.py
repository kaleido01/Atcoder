a, b= map(int, input().split("."))

if 0<=b<=2:
  print(a+"-")
elif 3<=b<=6:
  print(a)
else:
  print(a+"+")