import itertools

# 品物のデータ (容量, 値段)
items = [
    (4, 6), (8, 12), (3, 4), (5, 3), (9, 7), (2, 1), (3, 3), (1, 2), 
    (5, 7), (2, 3), (4, 4), (2, 2), (7, 10), (10, 13), (3, 5), (13, 16), 
    (11, 14), (8, 9)
]
# ナップサックの容量
capacity = 45 

max_price = 0
best_combination = []

# すべての組み合わせ（2^18 = 262,144通り）を試す 
for p in itertools.product([0, 1], repeat=18):
    total_weight = 0
    total_price = 0
    
    # 選択した品物の合計容量と値段を計算
    for i in range(18):
        if p[i] == 1:
            total_weight += items[i][0]
            total_price += items[i][1]
            
    # 容量制限内かつ、これまでの最大値段より高ければ更新
    if total_weight <= capacity:
        if total_price > max_price:
            max_price = total_price
            best_combination = p

# 結果を表示
print(f"最大値段: {max_price}")
print(f"選択した品物（1が入っている場所）: {best_combination}")