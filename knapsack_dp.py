# 品物のデータ (容量, 値段)
items = [
    (4, 6), (8, 12), (3, 4), (5, 3), (9, 7), (2, 1), (3, 3), (1, 2), 
    (5, 7), (2, 3), (4, 4), (2, 2), (7, 10), (10, 13), (3, 5), (13, 16), 
    (11, 14), (8, 9)
]
capacity = 45

# DPテーブルの初期化 (容量0から45まで)
dp = [0] * (capacity + 1)

# 動的計画法
for weight, price in items:
    for c in range(capacity, weight - 1, -1):
        dp[c] = max(dp[c], dp[c - weight] + price)

print(f"最大値段: {dp[capacity]}")
