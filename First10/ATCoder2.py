s = list(input())
count =0
ans = 0
for c in s:
  if c =="A" or c == "C" or c == "G" or c == "T":
    count +=1
  else:
    ans = max(ans, count)
    count = 0
ans = max(ans, count)
    
    
print(ans)