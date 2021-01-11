import sys
n = int(input())

res = [0] * 3
k = 0
sumketa=0
while(n > 0):
  keta = n % 10
  amari = keta % 3
  # if amari == 0:
  #   print(0)
  #   sys.exit()
  res[amari] +=1
  sumketa += amari
  k += 1
  n //= 10

if sumketa % 3 == 0:
  print(0)
elif sumketa % 3 == 1:
  if res[1] and k!=1 >= 1:
    print(1)
  elif res[2] and k!=2 >= 2:
    print(2)
  else:
    print(-1)
else:
  if res[2] and k!=1>= 1:
      print(1)
  elif res[1] and k!=2>= 2:
    print(2)
  else:
    print(-1)
  
    