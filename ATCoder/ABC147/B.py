s = input()

middle = len(s) //2
last = len(s)-1
count = 0

for i in range(middle):
  if s[i] != s[last-i]:
    count +=1

print(count)