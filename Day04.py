import time

# 붕어빵 재료별 소요 시간 (초 단위)
ingredient_times = {
    "피자": 60,
    "슈크림": 45,
    "단팥": 50,
    "초코릿": 55,
}

# 붕어빵 가격
price_per_pancake = 1000

# 사용자에게 붕어빵 종류와 개수를 입력받음
pancake_type = input("어떤 종류의 붕어빵을 원하시나요? (피자, 슈크림, 단팥, 초코릿): ")
pancake_quantity = int(input("몇 개를 주문하시겠습니까?: "))

# 붕어빵을 만드는데 걸리는 총 시간 계산
if pancake_type in ingredient_times:
    total_time = ingredient_times[pancake_type] * pancake_quantity
else:
    print("죄송합니다. 해당 종류의 붕어빵을 만들 수 없습니다.")
    exit()

# 시간을 분과 초로 변환
minutes = total_time // 60
seconds = total_time % 60

# 주문한 붕어빵 정보 출력
print(f"{pancake_type} 붕어빵 {pancake_quantity}개를 만드는데 {minutes}분 {seconds}초 걸렸습니다.")

# 주문 금액 계산
total_price = price_per_pancake * pancake_quantity

# 사용자에게 지불한 금액 입력
paid_amount = int(input("지불한 금액을 입력하세요: "))

# 거스름돈 계산
change = paid_amount - total_price

# 주문 정보 출력
print(f"금액은 {total_price}원이며, 받은 돈은 {paid_amount}원이고, 거스름돈은 {change}원 입니다.")
