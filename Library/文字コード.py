def s(n):
    return sum(ord(c) - ord('0') for c in n)
 
a, b = input().split()
print(max(s(a), s(b)))