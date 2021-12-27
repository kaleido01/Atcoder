import sys
n = int(input())

a = []
for x in range(n):
  b = list(map(str, input().split()))
  a.append(b)


ans = False


for i in range(n):
  for j in range(i, n-1):
    # print(i,j+1)
    if a[i][0] == a[j+1][0] and a[i][1] == a[j+1][1]:
      ans = True


if ans:
  print("Yes")
else:
  print("No")