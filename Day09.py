# 이중 배열 생성
matrix = []

# 이중 배열의 행과 열 수
rows = 3
cols = 4

# 이중 배열 채우기
for i in range(rows):
    row = []  # 새로운 행을 생성
    for j in range(cols):
        # 각 열에 값을 추가하고 싶다면, 여기에 값을 할당합니다.
        value = i * cols + j
        row.append(value)
    matrix.append(row)

# 이중 배열 출력
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end="\t")
    print()

# 특정 위치의 값에 접근
row_index = 1
col_index = 2
value = matrix[row_index][col_index]
print(f"matrix[{row_index}][{col_index}]의 값: {value}")

import random

# 이중 배열의 행과 열 수
rows = 5
cols = 6

# 이중 배열 생성 및 초기화
matrix = [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]

# 이중 배열 출력
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end="\t")
    print()

# 행의 합 출력
for i in range(rows):
    row_sum = sum(matrix[i])
    print(f"행 {i}의 합: {row_sum}")

# 열의 합 출력
col_sums = [sum(matrix[i][j] for i in range(rows)) for j in range(cols)]
for j in range(cols):
    print(f"열 {j}의 합: {col_sums[j]}")

# 첫 번째 행렬 (3x3)
matrix1 = [[2, 3, 4],
           [5, 6, 7],
           [8, 9, 10]]

# 두 번째 행렬 (3x2)
matrix2 = [[10, 20],
           [30, 40],
           [50, 60]]

# 결과 행렬 초기화 (3x2)
result = [[0, 0],
          [0, 0],
          [0, 0]]

# 행렬 곱셈 수행
for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            result[i][j] += matrix1[i][k] * matrix2[k][j]

# 결과 행렬 출력
print("행렬 곱셈 결과:")
for row in result:
    print(row)
