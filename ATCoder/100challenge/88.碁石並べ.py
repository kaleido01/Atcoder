n = int(input())

c = [int(input()) for _ in range(n)]


ans = [0] * n
ans[0] = 1

countingIndex = 0
rightColor = c[0]
leftColor = c[0]
for i in range(1, n):
  putColor = c[i]
  # 隣と同じ石を置く
  if putColor == rightColor:
    ans[countingIndex] += 1
  # 偶数番目の時は左の色を確認する
  elif (i+1) % 2 == 0:
    # 異なる石を置く場合
    if countingIndex == 0:
      ans[countingIndex] +=1
      leftColor = putColor
    else:
      ans[countingIndex - 1] += ans[countingIndex] + 1
      ans[countingIndex] = 0
      countingIndex -= 1
    
  else:
    countingIndex += 1
    ans[countingIndex] = 1

  rightColor = putColor
res = 0
# print(ans)
for i in range(n):
  if i % 2 ==0:
    res += ans[i]
    
if leftColor == 0:
  print(res)
else:
  print(n-res)

    
  




