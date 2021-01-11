n = input()

s = 0
for v in n:
  s += int(v)

# sumn = 0
# while (n > 0):
#   sumn += n % 10
#   n //= 10

if s % 9 == 0:
  print("Yes")
else:
  print("No")


