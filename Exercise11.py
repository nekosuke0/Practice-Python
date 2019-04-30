n = int(input("数字を入力してください:"))
for p in range(2, n):
    if n % p == 0:
        print(str(n) + "は合成数です。")
        break
    else:
        print(str(n) + "は素数です。")
        break