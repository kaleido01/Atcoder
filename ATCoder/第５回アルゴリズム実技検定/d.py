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

s =[]
for i in range(n):
  x = input()
  count = 0
  for j in x:
    if j == "0":
      count +=1
    else:
      break
  s.append([int(x),count,x])

s = sorted(
  s,
  key = lambda s: (s[1]),
  reverse = True
)

s = sorted(
  s,
  key = lambda s: (s[0]),
)
  

for i in range(n):
  print(s[i][2])

# p = "0100000000"
# print(int(p))