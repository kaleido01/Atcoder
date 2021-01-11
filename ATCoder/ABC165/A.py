import sys
n = int(input())

a, b = map(int, input().split())
for i in range(a, b+1):
  if i%n == 0:
    print("OK")
    sys.exit()

print("NG")


