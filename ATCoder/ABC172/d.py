

n = int(input())

counter = [0] * (n+1)


# for i in range(1, n+1):
#     counter[i] = n//i
    
    
# ans = 0
# for i in range(1,n+1):
#     ans += counter[i]
  
# print(counter)  
# print(ans)

def f(n):
    return n * (n+1) // 2
ans = 0


for i in range(1, n+1):
    ans += i * f(n // i)

print(ans)
