import random

k = 10000  # 試行回数
for j in range(10): # k回の試行を10回繰り返し，すべての結果を出力する
  sum_prize_total = 0  # 「100ゲームの賞金額の合計」の総和
  for i in range(k):
      prize_total = 0  # 100ゲームの賞金額の合計
      for game in range(100):  # 100ゲーム繰り返す
          prize = 2  # 1ゲームの賞金額
          while True:
              if random.randint(1, 2) == 1:
                  prize = prize * 2
              else:
                  break
          prize_total = prize_total + prize
      sum_prize_total = sum_prize_total + prize_total
  print(sum_prize_total / k)
