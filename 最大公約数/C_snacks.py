import math
import sys
a, b = map(int, input().split())

#最小公倍数は最大公約数を用いて求めることができます。A,Bの最大公約数を G とおくと、A,Bの最小公倍数を L として、
#G×L=A×B




print(a*b // math.gcd(a,b))
