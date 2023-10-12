import random

# 랜덤한 숫자 생성
secret_number = random.randint(1, 100)
attempts = 0

print("1부터 100까지의 숫자 중에서 비밀 숫자를 맞춰보세요.")

while True:
    try:
        guess = int(input("추측한 숫자를 입력하세요: "))
        attempts += 1

        if guess < secret_number:
            print("더 큰 숫자를 선택하세요.")
        elif guess > secret_number:
            print("더 작은 숫자를 선택하세요.")
        else:
            print(f"정답입니다! {attempts}번 시도하셨습니다.")
            break
    except ValueError:
        print("올바른 숫자를 입력하세요.")

