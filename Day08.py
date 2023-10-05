#이중 배열은 다른 배열을 요소로 포함하는 배열
# 이를 통해 표나 행렬과 같은 다차원 데이터를 표현할 수 있습니다. 
# 파이썬에서 이중 배열은 리스트의 리스트로 구현됩니다. 

# 3x3 이중 배열 생성
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# 이중 배열의 요소에 접근
print(matrix[0][0])  # 첫 번째 행의 첫 번째 열 (1)
print(matrix[1][2])  # 두 번째 행의 세 번째 열 (6)

# 이중 배열 순회 (행렬 출력)
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()  # 한 행을 출력한 후 줄 바꿈

# 붕어빵 가게 이중 배열
bungeoppang_shop = [
    ["단팥 붕어빵", 10],
    ["크림 붕어빵", 15],
    ["치즈 붕어빵", 8],
    ["팥크림 붕어빵", 12]
]

# 이중 배열 순회하여 붕어빵 정보 출력
for bungeoppang in bungeoppang_shop:
    name = bungeoppang[0]
    quantity = bungeoppang[1]
    print(f"{name}: {quantity} 개")
