a, b= map(int, input().split("."))

if 0<=b<=2:
  print(str(a)+"-")
elif 3<=b<=6:
  print(a)
else:
  print(str(a)+"+")