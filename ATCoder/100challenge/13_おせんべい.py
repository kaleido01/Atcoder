import copy
r, c = map(int, input().split())
 
 
s = [list(map(int, input().split())) for _ in range(r)]
 
 
def reverse(sc,w,h):
    if sc[h][w] == 0:
        sc[h][w] = 1
    else:
        sc[h][w] = 0
    return sc
 
ans = 0
# i行全てについて全探索
for i in range(2 ** r):
    # 縦列 1か確認して
    sc = [[v for v in x] for x in s]
    for j in range(r):
        #1になっているものの横列をひっくり返す
        if (i>>j) & 1:
            for k in range(c):
                reverse(sc,k,j)
 
 
    #j列に対して和が半分より大きければひっくり返す
    for j in range(c):
        if sum([x[j] for x in sc]) > r/2:
            for k in range(r):
                reverse(sc,j,k)
                 
    #操作を終えたq配列の合計の面枚数を数えて最大値を更新(ただし裏側0がカウントされるので全体から引いている)
    ans = max(ans, (r*c-sum(map(sum, sc))))
        
print(ans)