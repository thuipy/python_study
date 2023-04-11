number = 23
running = True

while running:
    guess = int(input("请输入一个整数："))
    if guess == number:
        print("祝贺你，猜对了")
        print("但你不会获得奖励！")
        running = False
    elif guess < number:
        print("猜错了，它是一个更大一点的数。")
    else:
        print("猜错了，它是一个更小的数。")
else:
    print("while循环结束。")

print("Done")
