# 붕어빵을 만들 개수를 지정합니다.
num_bungeoppang = 3

# 외부 루프: 붕어빵을 만들 개수만큼 반복합니다.
for i in range(num_bungeoppang):
    # 내부 루프: 붕어빵을 만드는 과정을 나타냅니다.
    for j in range(5):  # 예를 들어, 붕어빵을 5번 돌면서 굽는다고 가정합니다.
        print(f"붕어빵 {i+1}번째를 굽는 중...({j+1}/5)")

    # 붕어빵 하나가 완성될 때마다 메시지를 출력합니다.
    print(f"붕어빵 {i+1}번째가 완성되었습니다!")

print("모든 붕어빵이 만들어졌습니다.")

num_bungeoppang = 3

for i in range(num_bungeoppang):
    print(f"붕어빵 {i+1}번째를 만듭니다.")
    
    for ingredient in ["반죽을 만듭니다.", "팥을 넣습니다.", "굽습니다.", "완성합니다."]:
        print(ingredient)
    
    print(f"붕어빵 {i+1}번째가 완성되었습니다!")

print("모든 붕어빵이 만들어졌습니다.")

num_bungeoppang = 3
bungeoppang_count = 0

while bungeoppang_count < num_bungeoppang:
    print(f"붕어빵 {bungeoppang_count+1}번째를 만듭니다.")
    
    step = 1
    while step <= 4:
        if step == 1:
            print("반죽을 만듭니다.")
        elif step == 2:
            print("팥을 넣습니다.")
        elif step == 3:
            print("굽습니다.")
        else:
            print("완성합니다.")
        
        step += 1
    
    print(f"붕어빵 {bungeoppang_count+1}번째가 완성되었습니다!")
    bungeoppang_count += 1

print("모든 붕어빵이 만들어졌습니다.")
