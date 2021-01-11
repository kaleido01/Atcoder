n, m = map(int,input().split())



mod = 10**9+7 #出力の制限
#初期化として考えられる最大のnを入力nCr
class Combination:
  mod = 10**9+7 #出力の制限
  g1 = [1, 1] # 元テーブル
  g2 = [1, 1] #逆元テーブル
  inverse = [0, 1] #逆元テーブル計算用テーブル
  
  def __init__(self,n):
    for i in range(2, n + 1 ):
     self.g1.append( ( self.g1[-1] * i ) % self.mod )
     self.inverse.append( ( -self.inverse[self.mod % i] * (self.mod//i) ) % self.mod )
     self.g2.append( (self.g2[-1] * self.inverse[-1]) % self.mod )

  def cmb(self, n, r):
    if ( r < 0 or r > n ):
        return 0
    r = min(r, n - r)
    return self.g1[n] * self.g2[r] * self.g2[n-r] % self.mod
  
  def per(self, n, r):
    if ( r < 0 or r > n ):
        return 0
    return self.g1[n] * self.g2[n-r] % self.mod
  


c = Combination(5 * (10 ** 5) +10)

ans =0
for i in range(n+1):
  # print("c.cmb(n,i)",c.cmb(n,i))
  # print("c.per(m-i,n-i)",c.per(m-i,n-i))
  # print((-1)**i)
  now = (-1)**i * c.cmb(n,i) % mod
  now *= c.per(m-i,n-i) % mod

  ans += now
  ans %= mod
  
ans *= c.per(m,n) % mod

print(ans % mod)
