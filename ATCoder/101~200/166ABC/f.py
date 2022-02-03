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


n, x, y, z= mapInt()
ans = []
a = [x, y, z]

x = "ABC"
# pに +1 q に-1
def add(p,q):
  a[p] += 1
  a[q] -= 1
  ans.append(x[p])

ss = []
for i in range(n):
  ss.append(input())
  
for i in range(n-1):
  s = ss[i]
  p,  q = 0, 1
  if s =="BC":
    p, q = 1,2
  elif s == "AC":
    q = 2
    
  if a[p] == 0 and a[q] == 0:
    print("No")
    sys.exit()
    
  if a[p] > a[q]:
    add(q,p)
  elif a[p] < a[q]:
    add(p,q)
  else:
    s = ss[i+1]
    np, nq = 0,1
    if s =="BC":
      np, nq = 1,2
    elif s == "AC":
      nq = 2
      
    if p == np or p == nq:
      add(p,q)
    elif q == nq or q == np:
      add(q,p)

s = ss[n-1]
p,  q = 0, 1
if s =="BC":
  p, q = 1,2
elif s == "AC":
  q = 2
  
if a[p] == 0 and a[q] == 0:
  print("No")
  sys.exit()
elif a[p] >= a[q]:
  add(q,p)
else:
  add(p,q)

print("Yes")
for v in ans:
  print(v)
        
    
    
  
