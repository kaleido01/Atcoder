# -*- coding: utf-8 -*-
from audioop import reverse
from re import X
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




n, K = mapInt()

sushi = {}

for i in range(n):
  t, d = mapInt()
  if t in sushi:
    sushi[t].append(d)
  else:
    sushi[t] = [d]
    
    

pq = []
for _, v in sushi.items():
  v.sort(reverse = True)
  for i in range(len(v)):
    if i == 0:
      heapq.heappush(pq, (-v[i], 1))
    else:
      heapq.heappush(pq, (-v[i], 0))
  


p = 0
ans = 0
cnt = 0
temp = 0
rest = []
already = []

#初回
# print(pq)
while(cnt < K):
  if not pq: break
  v, new = heapq.heappop(pq)
  # 種類数を追加する場合小さい順に見る
  if new:
    if p == 1:
      heapq.heappush(rest, v)
    else:
      temp += -v
      p +=1
      cnt +=1
  else:
    heapq.heappush(already, -v)
    cnt += 1
    temp += -v
    

ans = max(ans, temp + p ** 2)
# print(temp, p)
while((pq or rest) and p < K):
  
  if cnt < K:
    y = heapq.heappop(rest)
    temp += -y
    p +=1
    cnt +=1
    if cnt == K:
      ans = max(ans, temp + p ** 2)
      # print(temp, p)
    continue
  if rest:
    # 最小の値を除く
    if not already: break
    x = heapq.heappop(already)
    temp -= x
    # 種類数が増え最大の値を追加する。
    y = heapq.heappop(rest)
    temp += -y
    p +=1
    ans = max(ans, temp + p ** 2)
    # print(temp, p)
  else:
    v, new = heapq.heappop(pq)
    if new:
      # 最小の値を除く
      x = heapq.heappop(already)
      temp -= x
      p+=1
      temp += -v
      ans = max(ans, temp + p ** 2)
      # print(temp, p)
print(ans)