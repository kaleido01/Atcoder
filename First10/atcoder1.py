n = input()
a = list(map(int, input().split()))


a.sort(reverse=True)
aliceCount = 0
bobCount = 0

index = 0
for value in a:
    if index % 2 == 0:
        aliceCount += value
    else:
        bobCount += value
    index += 1

print(aliceCount - bobCount)
