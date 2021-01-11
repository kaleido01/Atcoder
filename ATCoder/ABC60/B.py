import sys
a,b,c = map(int, input().split())



count = [False] * 100

i=1
res= 0
while(True):
  res +=a
  d = res % b
  if d==c:
    print("YES")
    sys.exit()
  elif count[d]:
    print("NO")
    sys.exit()
  else:
    count[d] =True
