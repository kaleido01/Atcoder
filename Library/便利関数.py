
# 第二引数でソートをしてくれる
l = [(3, 4),(1, 1),(3, 9),(3, 5)]
l.sort(key= lambda array: array[1])


#　文字列逆順処理
s = "erg49tuaef"
s[::-1]


# 優先度付きキューの基本
# heapq.heapify(リスト)でリストを優先度付きキューに変換。
# heapq.heappop(優先度付きキュー (=リスト) )で優先度付きキューから最小値を取り出す。
# heapq.heappush(優先度付きキュー (=リスト) , 挿入したい要素)で優先度付きキューに要素を挿入。

a = [1, 6, 8, 0, -1]
heapq.heapify(a)  # リストを優先度付きキューへ
print(a)
# 出力: [-1, 0, 8, 1, 6] (優先度付きキューとなった a)

# 文字列結合
s = "".join(t)

#０除算に気をつけよう

# 改行出力は下記でもいける.正確には空白出力だが。
print(*ans)
