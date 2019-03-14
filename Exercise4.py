a = int(input("数字を入力してください："))

a_list = []

for i in range(1, a):
     if a % i == 0:
        a_list.append(i)

print(a_list)
