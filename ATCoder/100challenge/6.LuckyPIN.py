n= int(input())
s =list(input())
ans = 0
for i in range(1000):
  p = list(str(i))
  length = len(p)
  if length ==1:
    p.insert(0,"0")
    p.insert(0,"0")
  elif length ==2:
    p.insert(0,"0")
  x = 0
  for c in s:
    if c == p[x]:
        x +=1
    if x == 3:
      ans +=1
      break
print(ans)