import random

for i in range(10):
    k = 100000  # 試行回数
    sum_x = 0  # 離散一様乱数の値の総和
    for i in range(k):
        x = random.randint(1, 6)  # 離散一様乱数U{1, 2, 3, 4, 5, 6}の値を得る
        sum_x = sum_x + x
    print(sum_x / k)
