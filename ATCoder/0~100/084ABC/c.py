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
inithw = lambda h, w: [ listInt() for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]

YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1
from operator import itemgetter


n = int(input())

c =[0] * (n-1)
s =[0] * (n-1)
f =[0] * (n-1)

for i in range(n-1):
  x,y,z = mapInt()
  c[i] = x
  s[i] = y
  f[i] = z
  

# print(s)
for i in range(n-1):
  time = 0
  for j in range(i,n-1):
    # print(j)
    if time <= s[j]:
      time = s[j]
      # print("atime",time)
    
    if (time-s[j]) % f[j] != 0:
      time += f[j] - (time-s[j]) % f[j]
    
    # print("time",time)
    time += c[j]
  print(time)
  
  
print(0)