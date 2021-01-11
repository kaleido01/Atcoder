n = int(input())

########関数部分##############
def Base_10_to_n(X, n):
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n)+str(X%n)
    return str(X%n)
############################
 
 
#####関数をつかってみる．#####
######今回は二進数に変換######
is_ok = [0] * (10**5 +5)
# is_ok = [0] * (30)
for i in range(n+1):
  # for v in str(i):
  #   if v =="7":
  if "7" in str(i):
    is_ok[i] = 1
  x8 = Base_10_to_n(i, 8)
  if "7" in str(x8):
    is_ok[i] = 1

# print(is_ok)
# if sum(is_ok) == 0:
#   print(n)
# else:
print(n - sum(is_ok))

# print("17" in "7")