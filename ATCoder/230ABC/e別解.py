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


h, w, k = mapInt()

grid = inithw(h)

ans = h * w

# 今の配列に対して各グループにその列のホワイトチョコレートの数を追加してkを超えないか確認
def isAdd(w:int, y:int):
  groupIndex = 0
  b = a.copy()
  for j in range(h):
    b[groupIndex] += 1 if grid[j][w] == "1" else 0
    # print("b",b)
    if b[groupIndex] > k: return False
    if y >> j & 1:
      groupIndex +=1
  
  return True

def add(w:int, y:int):
  groupIndex = 0
  for j in range(h):
    a[groupIndex] += 1 if grid[j][w] == "1" else 0
    if y >> j & 1:
      groupIndex +=1


for y in range(1 << (h-1)):
  line = 0
  result = 0
  isImpossible = False
  for j in range(h-1):
    if (y >> j) & 1:
      line += 1
  # print(line)
  a = [0 for i in range(line+1)]
  
  result += line
  
  for x in range(w):
    if not isAdd(x, y):
      a = [0 for i in range(line+1)]
      if not isAdd(x,y):
        isImpossible = True
        break
      result += 1
    
    add(x,y)
      
  
  if isImpossible:continue
  # print(result)
  ans = min(ans, result)
        
    
print(ans)