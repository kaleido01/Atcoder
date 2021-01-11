import math
import sys
n = int(input())
an= list(map(int, input().split()))

#最小公倍数は最大公約数を用いて求めることができます。A,Bの最大公約数を G とおくと、A,Bの最小公倍数を L として、
#G×L=A×B

g = an[0]
for i in range(1,n):
  g = math.gcd(g,an[i])

print(g)
