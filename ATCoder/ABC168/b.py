k = int(input())
s = input()



if len(s) <= k:
  print(s)
else:
  news= s[0:k]
  news +="..."
  print(news)