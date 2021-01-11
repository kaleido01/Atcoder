n = int(input())
a = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))


def binary(v):
  i=0
  bit= [0] *30
  while (v>0):
    bit[i] = v%2
    i +=1
    v //=2
  return bit

for testIndex in range(q):
  canMake = False
  for i in range(2 ** n):
    bit = binary(i)
    if canMake:
      continue
    # print(bit)
    sum = 0
    for j in range(len(bit)):
      if bit[j]==1:
        sum += a[j]
    if sum== m[testIndex]:
      print("yes")
      canMake = True
  if not canMake:
    print("no")