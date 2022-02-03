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
s = input()

left = 0
right = n-1

ans = 0
while(left < right):
  #左側で最初にWになる場所をみつける
  while(left != right):
    # print(left, right)
    if s[left] == "W":
      break
    left += 1
  
  #右から最初にRになる位置を見つける
  while(left != right):
    if s[right] == "R":
      break
    right -= 1
  
  # print(left, right)
  if s[left] == "W" and s[right] == "R":
    ans += 1
    left +=1
    right -= 1
  
    
print(ans)
  