




# 条件を満たす限り右端を進める
# 条件を満たさなくなったら左端を条件を満たすまで進める


a = [3,7, 11, 1, 45]
n = len(a)

right = 0
for left in range(n):
    while (right < n and (right を 1 個進めたときに条件を満たす)):
        # 実際に right を 1 進める */
        # ex: sum += a[right];
        right += 1

    # break した状態で right は条件を満たす最大なので、何かする */
    # ex: res += (right - left);

    # left をインクリメントする準備 */
    # ex: if (right == left) ++right;
    # ex: else sum -= a[left];
