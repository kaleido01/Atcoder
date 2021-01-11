

def deleteStones(score):
  
  for stone in stones:
    sequense = 0
    maxSequence = [0,0]
    firstIndex = 0
    isFirst = True
    for j in range(4):
      # print(stone[j])
      if stone[j] != 0 and stone[j] == stone[j+1]:
        sequense += 1
        if isFirst:
          firstIndex = j
          isFirst = False
      else:
        if maxSequence[0]  < sequense:
          maxSequence = [sequense, firstIndex]
          sequense = 0
        isFirst  = True
      if j == 3:
        if maxSequence[0]  < sequense:
          maxSequence = [sequense, firstIndex]
    # print(maxSequence)
    if maxSequence[0] >= 2:
      firstIndex = maxSequence[1]
      num = stone[firstIndex]
      score += num * (maxSequence[0]+1)
      # print(firstIndex, maxSequence[0])
      for i in range(firstIndex,firstIndex + maxSequence[0] +1):
        stone[i] = 0
  return score
      

def dropStones():
  for index in range(5):
    for i in range(h-1,0,-1):
      if stones[i][index] != 0:
        continue
      for j in range(i,-1, -1):
        if stones[j][index] != 0:
          stones[j][index], stones[i][index] = stones[i][index], stones[j][index]
          break

while(True):
  h = int(input())
  if h == 0:
    break
  stones = [list(map(int, input().split())) for _ in range(h)]
  score = 0

  for _ in range(h+3):
    score = deleteStones(score)
    # print(stones)
    dropStones()
    # print(stones)
  # print(stones)
  print(score)
          