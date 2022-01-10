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

#d桁のパターン
#差が一桁

ok = []

for i in range(100):
  ok.append(i)
  

for i in range(100, 1000):
  s = str(i)
  if int(s[2]) - int(s[1]) == int(s[1]) - int(s[0]):
    ok.append(i)
  
for i in range(1000, 10000):
  s = str(i)

  if int(s[2]) - int(s[1]) == int(s[3]) - int(s[2]) == int(s[1]) - int(s[0]):
    ok.append(i)
  
for i in range(10000, 100000):
  s = str(i)

  if int(s[2]) - int(s[1]) == int(s[3]) - int(s[2]) == int(s[4]) - int(s[3]) == int(s[1]) - int(s[0]):
    ok.append(i)
  


ok.append(234567)
ok.append(345678)
ok.append(456789)
ok.append(987654)
ok.append(876543)
ok.append(765432)

ok.append(2345678)
ok.append(3456789)
ok.append(9876543)
ok.append(8765432)

ok.append(98765432)
ok.append(23456789)

for i in range(6, 20):
  
  x = []
  y = []
  if i <= 10:
    for j in range(i):
      y.append(str(j))
    l = "".join(y)
    ok.append(int(l[::-1]))
    
    for j in range(1, i):
      x.append(str(j))
    l = "".join(x)
    
    ok.append(int(l))
    ok.append(int(l[::-1]))
  
  for j in range(1, 10):
    s = str(j)*i
    ok.append(int(s))
  
ok.sort()
# print(ok)
for v in ok:
  if v >= n:
    print(v)
    sys.exit()
