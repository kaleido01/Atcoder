while(True):
  
  n = int(input())
  if n == 0:
    break

  c = [0 for _ in range(24 * 60 * 60 + 60 * 60 +1)]

  for i in range(n):
    s,e = map(str, input().split())
    h1, m1, s1 = s.split(":")
    count1 = int(h1)  * 60 *60 + int(m1) * 60 + int(s1)
    h2, m2, s2 = e.split(":")
    count2 = int(h2) * 60 * 60 + int(m2) * 60 + int(s2)
    
    # print(h1, m1,s1)
    # print(h2, m2,s2)
    # print(count1, count2)
    c[count1] +=1
    c[count2] -=1

  s = [0 for _ in range(24 * 60 * 60 + 60 * 60 +5)]

  for i in range(len(c)):
    s[i+1] = s[i] + c[i]
  # print(s)
  print(max(s))