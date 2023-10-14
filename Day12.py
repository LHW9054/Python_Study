import random

def up_down_game(attempts):
    # 1에서 100 사이의 무작위 숫자 생성
    secret_number = random.randint(1, 100)
    
    print("업다운 게임을 시작합니다. 1에서 100 사이의 숫자를 맞춰보세요!")
    
    for attempt in range(attempts):
        try:
            user_guess = int(input(f"시도 {attempt + 1}/{attempts}: 숫자를 입력하세요: "))
            
            if user_guess < secret_number:
                print("Up! 높은 숫자를 입력하세요.")
            elif user_guess > secret_number:
                print("Down! 낮은 숫자를 입력하세요.")
            else:
                print(f"축하합니다! {secret_number}를 맞췄습니다.")
                break
        except ValueError:
            print("올바른 숫자를 입력하세요.")
    
    else:
        print(f"모든 기회를 사용하셨습니다. 정답은 {secret_number}였습니다.")

if __name__ == "__main__":
    attempts = int(input("몇 번의 기회를 원하십니까? "))
    up_down_game(attempts)
