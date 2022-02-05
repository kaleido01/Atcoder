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

tate = [ [] for _ in range(w)]
yoko = [ [] for _ in range(h)]

start = [0, 0]
m = INF

l = []
done = {}
ma = {}
for i in range(n):
  r, c, a = mapInt()
  r, c = r-1, c-1
  tate[c].append((r, a))
  yoko[r].append((c, a))
  # iは最後の出力用
  l.append((r,c,a,i))
  done[r * 10 + c] = False
  ma[r * 10 + c] = -1
l.sort(key= lambda b: b[2])



# print(done)


def bfs(start, count):
  r, c, a = start
  
  c1 = count
  for vx in tate[c]:
    i, v = vx
    if done[i*10 +c]: continue
    if v <= a: continue
    if ma[i*10 +c] != -1:
      c1 = max(c1, ma[i*10 +c] + count + 1)
      continue
    done[i * 10 + c] = True

    c1 = max(c1, bfs((i, c, v), count+1))
    # count
    # print("hear1", c1)
    done[i * 10 + c] = False
  
  c2 = count
  for vy in yoko[r]:
    j, v = vy
    if done[r * 10 + j]: continue
    if v <= a: continue
    if ma[r*10 +j] != -1: 
      c2 = max(c2, ma[r*10 +j] + count + 1)
      continue
    done[r * 10 + j] = True
    c2 = max(c2, bfs((r, j, v), count+1))
    # print("hear2", c2)
    done[r * 10 + j] = False

  m = max(count, c1, c2)
  ma[r*10 + c] = m - count
  return max(count, c1, c2)
    
    

ans = [0] * n
for lv in l:
  r, c, a, index = lv
  done[r * 10 + c] = True

  value = bfs((r, c, a), 0)
  
  ans[index] = value

# print(ma)
for a in ans:
  print(a)