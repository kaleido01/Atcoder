
from itertools import combinations, permutations, combinations_with_replacement
import math
w, h = map(int, input().split())

mod = 10**9 +7
#組み合わせ総数

def factorial(n):
  ans = 1
  while(n != 1 or n != 0):
    ans *= n % mod
    n -=1
  return ans
def combinations_count(n, r):
    return math.factorial(n) // ((math.factorial(n - r) ) * (math.factorial(r)))

print(combinations_count(w+h-2, w-1) % mod)
