import math

n = int(input())



def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


array = make_divisors(n)
l = len(array)

short = math.inf

for i in range(l//2):
  short = min(short, array[i] + array[l - i -1])
  
if l % 2 == 1:
  short = min(short, array[l // 2] * 2)

print(short-2)
    
