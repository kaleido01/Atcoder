n = int(input())


ans = [-1] * 6
for i in range(n):
  t, ok = input().split()
  
  if t == "A" and ok == 'AC' and ans[0] == -1:
    ans[0] = i+1
  if t == "B" and ok == 'AC' and ans[1] == -1:
    ans[1] = i+1
  if t == "C" and ok == 'AC' and ans[2] == -1:
    ans[2] = i+1
  if t == "D" and ok == 'AC' and ans[3] == -1:
    ans[3] = i+1
  if t == "E" and ok == 'AC' and ans[4] == -1:
    ans[4] = i+1
  if t == "F" and ok == 'AC' and ans[5] == -1:
    ans[5] = i+1
    
print(*ans)