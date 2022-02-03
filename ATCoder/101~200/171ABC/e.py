n = int(input())


an = list(map(int, input().split()))

s = 0

for i in range(n):
  s = s ^ an[i]

for i in range(n):
  print(an[i] ^ s, end = " ")