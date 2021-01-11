# -*- coding: utf-8 -*-
import sys

sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
mapInt = lambda: map(int, input().split())
listInt = lambda: list(map(int, input().split()))

init0 = lambda n: [0 for _ in range(n)]
inithwv = lambda h, w, v: [[v for _ in range(w)] for _ in range(h)]
inithw = lambda h: [ list(input()) for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]
bit = lambda n, k:((n >> k) & 1) # nのkビット目
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1
from operator import itemgetter

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


X = int(input())


l = make_divisors(X)

for i in range(len(l)//2+1):
  q = min(l[i], l[-1 * i -1])
  # print(q)
  for j in range(-1 *q,200):
    # print(j)
    v = (j + q) ** 5 - j** 5
    # if  v > X:
    #   break
    if v == X:
      print(j+q, j)
      sys.exit()


