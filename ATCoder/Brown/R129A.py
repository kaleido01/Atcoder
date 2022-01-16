n, l, r = map(int,input().split())
 
def f(x):
    ans = 0
    x = str(bin(x)[2:])
    print(x)
    for i in range(len(x)):
      print(i)
      #最上位ビットが１同士なら小さくなるため、条件を満たす。
      if 2 ** i ^ n < n:
          ans += min(2 ** (i + 1) - 1, r) - 2 ** i + 1
    return ans
 
print(f(r) - f(l - 1))