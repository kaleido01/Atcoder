n, k = map(int, input().split())



s = [0]*(200010)
p = [0]*(200010)

tm = 0
for i in range(n):
  p, q, r = map(int, input().split())
  s[p] += r
  s[q] -= r
  tm = max(tm, q)
  


# c_sum = [0]
# for i in range(0,tm):
#   c_sum.append(c_sum[i] + s[i])
  
  
  
for i in range(0,tm):
  s[i+1] += s[i]
# print(s,t)
frag = True
for i in range(0,tm+1):
  if  s[i]>k:
    print("No")
    frag = False
    break

if frag:
  print("Yes")

# if max(s) > k:
#   print("No")
# else:
#   print("Yes")

