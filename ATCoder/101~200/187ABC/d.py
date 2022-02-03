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

YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1
from operator import itemgetter


n = int(input())

a = [0] * n
b = [0] * n

suma = 0
sumb = 0

b2a = []
for i in range(n):
  x, y = mapInt()
  suma += x
  a[i] = x
  b[i] = y
  b2a.append((2*x+y,i))
  
  
  
  
sorted_data = sorted(b2a, key=lambda x:x[0],reverse = True)

# print(sorted_data)

count =1
for data in sorted_data:
  v, index = data
  suma -= a[index]
  sumb += a[index] + b[index]
  
  if suma < sumb:
    print(count)
    break
  else:
    count += 1