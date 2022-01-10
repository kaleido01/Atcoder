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


h, w, n = mapInt()

query = []

for i in range(n):
  r, c, a = mapInt()
  # iは最後の出力用
  query.append((r,c,a,i))
query.sort(key= lambda x: x[2], reverse = True)



now = INF
rows = {}
columns = {}
ans = [0] * n


# print(query)

# 同じ値をまとめて入れるための一時退避用
buf = []
for i in range(n):
  r, c, a, index = query[i]
  
  # 値が変わった場合、bufに入れておいた同じ値のコマの全てを確定させる
  if now != a:
    for rr, cc, val in buf:
      if rr in rows:
        rows[rr] = max(rows[rr], val)
      else:
        rows[rr] = val
      if cc in columns:
        columns[cc] = max(columns[cc], val)
      else:
        columns[cc] = val
    buf = []
    now = a
  
  temp = 0
  
  if r in rows:
    temp = max(temp, rows[r] + 1)
  
  if c in columns:
    temp = max(temp, columns[c] + 1)
  
  buf.append((r, c, temp))
  ans[index] = temp
  
print(*ans)
