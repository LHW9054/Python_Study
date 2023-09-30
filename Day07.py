#배열(리스트)생성
my_list = [1, 2, 3, 4, 5]

#요소 추가
#append(): 리스트의 끝에 요소를 추가합니다.
my_list.append(6)

# 요소 삭제
# remove(): 특정 요소를 삭제합니다.
my_list.remove(3)  # 3을 삭제

#pop(): 지정된 인덱스의 요소를 삭제하고 반환합니다.
popped_element = my_list.pop(2)  # 인덱스 2의 요소를 삭제하고 반환

#인덱싱과 슬라이싱
#인덱스로 요소에 접근하거나 슬라이싱으로 일부분을 추출할 수 있습니다.
element = my_list[1]  # 인덱스 1의 요소에 접근
sub_list = my_list[1:4]  # 인덱스 1부터 3까지의 요소를 추출

#길이 확인
#len(): 리스트의 길이를 반환합니다.
length = len(my_list)

# 정렬
# sort(): 리스트를 정렬합니다.
my_list.sort()

#sorted(): 정렬된 새로운 리스트를 반환합니다.
sorted_list = sorted(my_list)

# 역순
# reverse(): 리스트의 순서를 역으로 바꿉니다.
my_list.reverse()

# 검색
# index(): 특정 요소의 인덱스를 찾습니다.
index = my_list.index(1)  # 값 1의 인덱스를 찾음

# 존재 여부 확인
# in 연산자를 사용하여 특정 요소의 존재 여부를 확인할 수 있습니다.
if 3 in my_list:
    print("3이 리스트에 있습니다.")

#리스트 복제
#리스트를 복제하려면 슬라이싱을 사용하거나 copy() 메서드를 사용할 수 있습니다.
copy_of_list = my_list[:]  # 슬라이싱을 사용한 복제

# 학생 성적 리스트 생성
student_grades = [85, 92, 78, 90, 88]

# 성적 추가
student_grades.append(95)

# 성적 평균 계산
average_grade = sum(student_grades) / len(student_grades)

# 가장 높은 성적 찾기
highest_grade = max(student_grades)

# 가장 낮은 성적 찾기
lowest_grade = min(student_grades)

# 특정 성적의 인덱스 찾기
grade_to_find = 78
if grade_to_find in student_grades:
    index = student_grades.index(grade_to_find)
else:
    index = -1

# 성적 정렬
sorted_grades = sorted(student_grades)

# 성적 출력
print("학생 성적:", student_grades)
print("새로운 성적 추가 후:", student_grades)
print("평균 성적:", average_grade)
print("가장 높은 성적:", highest_grade)
print("가장 낮은 성적:", lowest_grade)
if index != -1:
    print(f"{grade_to_find}의 인덱스:", index)
else:
    print(f"{grade_to_find}는 찾을 수 없습니다.")
print("성적 정렬:", sorted_grades)