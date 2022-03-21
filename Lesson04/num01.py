import random
print("数あてゲームを始めます")
print("答えの範囲は1~100です")
answer = random.randrange(start = 1, stop = 100)

guess = int(input("あなたが予想する数字："))
tries = 1

while(guess != answer):
  if(guess > answer):
    print("あなたの予想した数は答えより大きいです")
  else:
    print("あなたの予想した数は答えより小さいです")

  tries = tries + 1
  guess = int(input("あなたが予想する数字："))


print("正解です。答えは{}".format(answer))
print("あなたの試行回数は{}でした".format(tries))