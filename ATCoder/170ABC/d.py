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
inithw = lambda h, w, v: [ listInt() for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]

YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1
from operator import itemgetter

n = int(input())

a = listInt()
# a.sort()

yakusuu = [False for i in range(10**6 + 5)]


for i in range(n):
  if yakusuu[a[i]] != 0:
    yakusuu[a[i]] += 1
    continue
  for j in range(a[i], 10**6+5, a[i]):
    yakusuu[j] += 1

ans = 0
for i in range(n):
  if yakusuu[a[i]] == 1:
    ans += 1
    
# print(yakusuu)
print(ans)

# def make_divisors(n):
#     lower_divisors , upper_divisors = [], []
#     i = 1
#     while i*i <= n:
#         if n % i == 0:
#             lower_divisors.append(i)
#             if i != n // i:
#                 upper_divisors.append(n//i)
#         i += 1
#     return lower_divisors + upper_divisors[::-1]



# ans = 0
# for i in range(n):
#   r = make_divisors(a[i])
#   # print(r)
#   frag = True
#   if i != n-1:
#     if a[i+1] == a[i]:
#       yakusuu[a[i]] = True
#       continue
#   for v in r:
#     if v == 1:continue
#     if yakusuu[v]:
#       frag = False
#       continue
#   yakusuu[a[i]] = True
#   if frag:
#     ans += 1
    
# print(ans)
