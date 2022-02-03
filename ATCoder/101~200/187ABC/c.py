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

sdict={}


for i in range(n):
  s = input()
  isbikkuri = False
  if s[0] == "!":
    isbikkuri = True
  
  if isbikkuri:
    x = s[1:]
    if x in sdict:
      v = sdict[x]
      if v == 1:
        print(x)
        sys.exit()
    else:
      sdict[x] = 2
  else:
    if s in sdict:
      v = sdict[s]
      if v == 2:
        print(s)
        sys.exit()
    else:
      sdict[s] = 1
        
      
print("satisfiable")