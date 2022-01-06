"""nを素因数分解"""
"""2以上の整数n => [[素因数, 指数], ...]の2次元リスト"""
""" 計算量は O(√n)"""

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

factorization(24) 



"""nの約数を列挙"""
""" 計算量は O(√n)"""
def divisor_list_s(num):
    divisors = []
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            divisors.append(i)  
            if i**2 == num:
                continue
            divisors.append(int(num/i))
#     return divisors # 昇順にしなくてよいならソートは不要
    return sorted(divisors) # 昇順にしたいときはソートする
divisor_list_s(36)

"""nの約数を列挙"""
""" 計算量は O(√n)"""
def eratosthenes(n):
    count = [0] * n
    primes = []
    for i in range(2, n):
        if count[i] != 0: continue
        primes.append(i)
        #　iを因数にもつ全ての値に+1する。
        for j in range(i, n, i):
            count[j] += 1
        
    return count, primes
divisor_list_s(36)