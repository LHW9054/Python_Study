# 붕어빵 가게에서 파는 붕어빵 종류 배열
bungeoppang_menu = ["단팥 붕어빵", "슈크림 붕어빵", "치즈 붕어빵", "야채 붕어빵"]

# 붕어빵 가게의 재고량 배열
inventory = [10, 5, 8, 3]

# 고객이 주문한 붕어빵 종류
customer_order = "슈크림 붕어빵"

# 주문한 붕어빵이 메뉴에 있는지 확인
if customer_order in bungeoppang_menu:
    print(customer_order + "을/를 주문하셨습니다.")
    
    # 주문한 붕어빵의 인덱스 찾기
    order_index = bungeoppang_menu.index(customer_order)
    
    # 주문한 붕어빵의 재고량 확인
    if inventory[order_index] > 0:
        print("주문하신 " + customer_order + "가 있습니다. 주문을 진행합니다.")
        
        # 주문한 붕어빵 재고 감소
        inventory[order_index] -= 1
        print(customer_order + "이/가 나왔습니다. 재고가 1 감소했습니다.")
    else:
        print("죄송합니다. 주문하신 " + customer_order + "는 품절되었습니다.")
else:
    print("죄송합니다. 주문하신 " + customer_order + "은/는 메뉴에 없습니다.")

    # 붕어빵 가게에서 파는 붕어빵 종류 배열
bungeoppang_menu = ["단팥 붕어빵", "슈크림 붕어빵", "치즈 붕어빵", "야채 붕어빵"]

# 붕어빵 가게의 재고량 배열
inventory = {
    "단팥 붕어빵": 10,
    "슈크림 붕어빵": 5,
    "치즈 붕어빵": 8,
    "야채 붕어빵": 3
}

# 고객 주문 리스트
customer_orders = ["단팥 붕어빵", "치즈 붕어빵", "딸기 붕어빵"]

# 주문 처리
for order in customer_orders:
    if order in bungeoppang_menu:
        if inventory[order] > 0:
            print(order + "을/를 주문하셨습니다. 주문을 진행합니다.")
            inventory[order] -= 1
            print(order + "이/가 나왔습니다. 재고가 1 감소했습니다.")
        else:
            print("죄송합니다. 주문하신 " + order + "는 품절되었습니다.")
    else:
        print("죄송합니다. 주문하신 " + order + "은/는 메뉴에 없습니다.")

# 붕어빵 가게에서 파는 붕어빵 종류 배열
bungeoppang_menu = ["단팥 붕어빵", "슈크림 붕어빵", "치즈 붕어빵", "야채 붕어빵"]

print("분어빵 가게 메뉴:")
for bungeoppang in bungeoppang_menu:
    print("- " + bungeoppang)

print("어떤 붕어빵을 주문하시겠습니까?")

# 붕어빵의 가격 배열
bungeoppang_prices = {
    "단팥 붕어빵": 1500,
    "슈크림 붕어빵": 1800,
    "치즈 붕어빵": 2000,
    "야채 붕어빵": 1700
}

# 고객이 가지고 있는 할인 쿠폰
coupon = "20% 할인"

# 고객이 주문한 붕어빵
customer_order = "슈크림 붕어빵"

# 주문 가격 계산
if customer_order in bungeoppang_prices:
    price = bungeoppang_prices[customer_order]
    if coupon == "20% 할인":
        discounted_price = price * 0.8
        print(customer_order + "의 가격은 " + str(discounted_price) + "원입니다.")
    else:
        print(customer_order + "의 가격은 " + str(price) + "원입니다.")
else:
    print("죄송합니다. 주문하신 " + customer_order + "은/는 메뉴에 없습니다.")

