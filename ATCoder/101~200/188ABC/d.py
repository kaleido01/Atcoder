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

N, C = mapInt()

# a = [0] * N
# b = [0] * N
# c = [0] * N

r = []
for i in range(N):
  x, y, z = mapInt()
  r.append([x,z])
  r.append([y+1,-1 * z])
  
r.sort()

# print(r)

ans = 0
now = 0
cur = 0

r.append([-1,0])

for i in range(2 * N):
  if r[cur][0] == -1:
    break
  nday = r[cur][0]
  now += r[cur][1]
  while(r[cur][0] == r[cur+1][0]):
    cur += 1
    now += r[cur][1]
    
  # print(now,r[cur][0], nday)
  if now <= C:
    ans += (r[cur+1][0] - nday) * now
  else:
    ans += (r[cur+1][0] - nday) * C
  cur += 1

print(ans)