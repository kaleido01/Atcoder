
"""二分探索法"""
"""基本的にはisOkの条件をいじる。"""
""" イメージとしてはある条件を設定したときにデフォルトのような形だとある閾値よりaiが小さい場合OKが返される。そのため範囲の左側にOKが並ぶようにok = -1としてある"""
""" 一方で不等号逆にする場合、ある閾値よりaiが大きい場合にOKが返されるため、右側にOKが並ぶようにok = len(a)になる"""
""" この時、okで返されるのはデフォルトだと条件を満たす最大の値、すなわち左側には閾値以下の値が並んでおりその中で一番大きな値がOKになる"""
""" 逆の場合、左には条件を満たさない値が並んでおりOKは条件を満たし始める最も小さい値になることが推測できる。"""

def isOk(index, key):
  """不等号を入れ替える場合は呼び出し側のOKとNGのmiddleも入れ替える"""
  return a[index] <= key
  # return a[index] >= key


def binary_search(v):
    ok = -1
    ng = len(a)
    # ng = -1
    # ok = len(a)
    while(abs(ok-ng) > 1):
      middle = (ok + ng) // 2
      if isOk(middle, v):
        ok = middle
      else:
        ng = middle
    return ok
        
        
        
a = [1, 2, 7, 7, 9, 12, 23, 23, 23, 23, 40]
print(binary_search(23)) # 0 九番目の23は条件を満たす最大値
print(binary_search(23)) # 0 6番目の23は条件を満たす最小値 