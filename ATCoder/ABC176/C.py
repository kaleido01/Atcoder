n = int(input())

an = list(map(int, input().split()))

s = 0

for i in range(len(an)):
  if i == 0:
    currentMin = an[i]
  else:
    if currentMin > an[i]:
      s += currentMin - an[i]
    else:
      currentMin = an[i]

print(s)