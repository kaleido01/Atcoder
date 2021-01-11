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
inithw = lambda h, w: [ listInt() for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]

YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1
from operator import itemgetter


q = int(input())
maxN= 10 ** 5 +10
like2017 = [False for i in range(maxN)]


"""nを素因数分解"""
"""2以上の整数n => [[素因数, 指数], ...]の2次元リスト"""
""" 計算量は O(√n)"""

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr


# print(factorization(17))
for i in range(3, maxN,2):
  # print(i)
  old1 = factorization(i)
  old2 = factorization((i+1) //2)
  
  if len(old1) == 1 and len(old2) == 1:
    if old1[0][1] ==1 and old2[0][1] ==1:
      like2017[i] = True
  
  

s = [0] * (maxN+1)

for i in range(1,maxN):
  s[i] = s[i-1] + (1 if like2017[i] else 0)
  
# print(s[0:50])
for i in range(q):
  a, b = mapInt()
  print(s[b] - s[a-1])