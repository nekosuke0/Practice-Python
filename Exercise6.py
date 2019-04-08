
word = input("文字を入力してください:")

kaibun = word[::-1]

if word == kaibun:
    print("回文です")
else:
    print('回文ではないです')