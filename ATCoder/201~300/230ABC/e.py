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

pt = n
ans = 0
while(pt >= 1):
  # 足し合わせるxを計算。これは最初にその値になるptでnを割ることで計算できる
  x = n // pt
  
  # 足し合わせるxが何個連続で出てくるかを計算する （例えばn = 30 の時 30で割ると x = 1, この値が連続して出るのは nをx+1で割った時 つまり１５である
  nextPt = n // (x + 1)
  ans += x * (pt - nextPt)
  
  # print(x, nextPt)
  
  pt = nextPt
print(ans)
