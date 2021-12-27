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
from collections import deque
import heapq

n, k = mapInt()
a = listInt()



count = [[0,i] for i in range(n+1)]

for i in range(n):
  x = a[i]
  count[x][0] += 1
  
now = -1
for i in range(n):
  if count[i][0] > 0:
    now = count[i][1]
  else:
    break

if now == -1:
  print(0)
  sys.exit()


count.sort()
# print(count, now)
ans = 0
used = 0
for i in range(n+1):
  kosuu, index = count[i]
  kosuu -= used
  if kosuu <= 0:
    continue
  if now < index:
    continue
  # if kosuu <=0:
  #   continue
    
  if k > kosuu:
    k -= kosuu
    used += kosuu
    ans += kosuu * (now + 1)
    now = index -1
  else:
    ans += kosuu * (now + 1)
    break


print(ans)

  

