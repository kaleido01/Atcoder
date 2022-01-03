def gcd(x,y):
  if y==0:     #[1]yが0の時はxを返す
    return x 
  else:#[2]y=0以外の時
    return gcd(y,x%y)