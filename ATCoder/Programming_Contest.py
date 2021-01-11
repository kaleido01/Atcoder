n, t = map(int, input().split())
a = list(map(int, input().split()))

halfN = n//2

w1 = [0 for _ in range(2 ** halfN)]
w2 = [0 for _ in range(2 ** (n - halfN))]


for i in range(2 ** halfN):
  value = 0
  for j in range(halfN):
    if (i >> j) & 1:
      value += a[j]
  w1[i] = value

for i in range(2 ** (n - halfN)):
  value = 0
  for j in range(n-halfN):
    if (i >> j) & 1:
      value += a[j+halfN]
  w2[i] = value


def isOK(index, value):
  return w2[index] >=value
def binary_search(x):
  ng = -1
  ok = len(w2)
  
  while( ok - ng ) >1:
    middle = (ok+ng)//2
    if isOK(middle, x):
      ok = middle
    else:
      ng = middle
  
  return ok

w2.sort()

ans = 0
for v in w1:
  if t - v < 0:
    continue
  index = binary_search(t - v)
  if index == -1:
    continue
  elif index == len(w2):
    ans = max(ans, v + w2[index-1])
  else:
    if v == 0 and index == 0:
      continue
    if v +w2[index] > t:
      if index ==0:
        ans = max(ans, v )
      else:
        ans = max(ans, v + w2[index-1])
    else:
      ans = max(ans, v + w2[index])
# print(w1,w2)
print(ans)

