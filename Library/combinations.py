from itertools import combinations, permutations, combinations_with_replacement
import math

#階乗
print(math.factorial(5))
# 120


#順列の総数
def permutations_count(n, r):
    return math.factorial(n) // math.factorial(n - r)

print(permutations_count(4, 2))
# 12


#順列のパターン生成
l = ['a', 'b', 'c', 'd']
pattern = list(permutations(l, 2))

#組み合わせ総数
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

print(combinations_count(4, 2))
# 6


#組み合わせパターン生成
c_list = list(combinations(l, 2))

print(c_list)
# [('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd'), ('c', 'd')]

print(len(c_list))
# 6

# 重複組み合わせパターン総数
def combinations_with_replacement_count(n, r):
    return combinations_count(n + r - 1, r)

print(combinations_with_replacement_count(4, 2))
# 10

# 重複組み合わせパターン生成
h_list = list(combinations_with_replacement(l, 2))