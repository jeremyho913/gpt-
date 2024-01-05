import random

def guess_the_number():
    # 生成一個1到100之間的隨機數字
    secret_number = random.randint(1, 100)
    
    print("歡迎來到猜數字遊戲！")
    print("我已經選擇了一個1到100之間的數字，你來猜猜是多少吧。")

    attempts = 0

    while True:
        # 玩家猜測數字
        guess = int(input("請輸入你的猜測: "))
        attempts += 1

        # 檢查猜測結果
        if guess < secret_number:
            print("太小了，再猜猜。")
        elif guess > secret_number:
            print("太大了，再猜猜。")
        else:
            print(f"恭喜你猜對了！你用了{attempts}次猜中了數字 {secret_number}。")
            break

if __name__ == "__main__":
    guess_the_number()
