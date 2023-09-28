#파이썬 요약
#파이썬 은 1991년에 발표된 인터프리터 방식의 프로그래밍 언어이다
#파이썬은 강력한 라이브러리와 풍부한 생태계를 통해 데이터를 수집하고 분석하며 시각화 할수 있다
#다른 프로그래밍 언어에 비해 비교적 쉽고 간편하게 사용할수 있다
#창시자는 네덜란드의 프로그래머 귀도 반 로섬(Guido van Rossum)
#1989년 크리스마스 주에, 연구실이 닫혀있어서 심심한 김에 만든 프로그래밍 언어이다
#파이썬 로고의 뱀은 비단뱀 이며
#창시자인 귀도 반 로섬(Guido van Rossum)이 컴퓨터 프로그래밍 언어의 이름을 정할 때 
#자신이 좋아하는 코미디쇼인 "Monty Python's Flying Circus"에서 영감을 받았기 때문입니다
#파이썬의 주요 특징
#1.읽기 쉬운 문법: 파이썬의 문법은 간결하고 가독성이 높아 초보자에게도 쉽게 접근할 수 있습니다. 이러한 특징은 코드를 작성하고 이해하기 쉽게 만듭니다.
#2.다양한 라이브러리와 모듈: 파이썬은 다양한 라이브러리와 모듈을 포함하고 있어, 개발자들은 이미 작성된 코드를 재사용하여 개발 속도를 높일 수 있습니다. 
#       특히 데이터 과학 및 인공 지능 분야에서 널리 사용되는 라이브러리인 NumPy, pandas, TensorFlow, 등이 있습니다.
#3.플랫폼 독립적: 파이썬은 다양한 운영 체제에서 동작하며, 플랫폼 간 이식성을 가지고 있습니다. 이는 어떤 운영 체제에서도 파이썬 코드를 실행할 수 있음을 의미합니다.
#4.동적 타이핑: 파이썬은 변수의 데이터 타입을 명시적으로 선언하지 않아도 되므로 개발자가 더 유연하게 코드를 작성할 수 있습니다.
#5.커뮤니티와 생태계: 파이썬은 활발한 개발자 커뮤니티와 풍부한 온라인 자료로 지원되며, 문제 해결과 학습을 돕는 리소스가 풍부합니다.

# 파이썬의 장점
#1.빠른 개발 속도: 파이썬의 간결한 문법과 다양한 라이브러리는 개발 속도를 높입니다. 빠른 프로토타이핑이 가능하므로 빠른 시장 진입이 가능합니다.
#2.다양한 응용 분야: 파이썬은 웹 개발, 데이터 분석, 인공 지능, 자동화, 게임 개발 등 다양한 응용 분야에서 사용됩니다.
#3.커뮤니티 지원: 파이썬 개발자 커뮤니티는 활발하며, 다양한 라이브러리와 도구를 공유하고 업데이트합니다.
#4.크로스 플랫폼 호환성: 파이썬은 다양한 운영 체제에서 동작하므로 개발자들은 특정 플랫폼에 제한받지 않고 작업할 수 있습니다.

#파이썬의 단점
#1.성능: 파이썬은 C나 C++과 같은 컴파일러 언어에 비해 실행 속도가 상대적으로 느립니다. 높은 성능을 요구하는 애플리케이션에는 적합하지 않을 수 있습니다.
#2.GIL (Global Interpreter Lock): CPython 인터프리터에서는 GIL이라는 제한적인 락이 있어 멀티스레딩 환경에서 병렬 처리가 제한됩니다. 이로 인해 다중 CPU 코어를 효율적으로 활용하지 못할 수 있습니다.
#3.모바일 앱 개발: 파이썬은 주로 서버 측 및 데스크톱 애플리케이션 개발에 사용되며, 모바일 앱 개발에는 주로 다른 언어가 사용됩니다

#출력 주석 주석처리 줄바꿈 줄복사 자료형 연산자 제어 input

#주석처리 방법
#을 사용해서 주석처리 하기
print("안녕하세요 파이썬!") #뒤에 있는 것은 주석처리

"""
주석처리 된다
print("Hello World!!!")
"""

'''
주석처리 된다
print("Hello World!!!")
'''

# 주석 단축키 ctrl + /
# #출력하는법 =
# 줄 복사 = option + shift + 방향키(⬆️ ⬇️)
# 줄 이동 = option + 방향키(⬆️ ⬇️)
# 줄 삭제 = command + x
# 이전으로 = Command + z
# 탭 닫기: Command + W
# 모든 탭 닫기: Option + Command + W
# 디버깅 없이 실행 : fn + control + f5
# 터미널 로그 지우기 : command + k
# 아랫줄로 이동 : command + enter
# 탐색창 : command + b

# 자료형을 명시적으로 선언하지 않습니다.
# 파이썬 은 ;(세미콜론)을 작성 하지 않아도 된다
# 파이썬은 
num1 = 1
num2 = 3.0
num3 = 0.1
num4 = num1 + num2 + num3
str1 = "Hello world"
str2 = "1234567890"
print(num1)
print(num2)
print(num3)
print(num4)
print(str1)
print(str2)

# 수치 자료형 : int, float, complex
# 불 자료형 : bool
# 군집 자료형 : str, list, tuple, set, dictionary

#자료형 출력하기
print(type(str1)) # 출력문 = <class 'str'>

#문자열 길이 출력하기
print(len(str1)) # 출력문 = 11

# 연산자
a = 1
b = 2
c = a + b
print(c) # 3
#덧셈
print(a + b) #3
#뺄셈
print(a - b) #-1
#곱하기
print(a * b) #2
#나눗셈
print(a / b) #0.5
#정수나눗셈
print(a // b) #0
#나머지
print(a % b) # 1
#거듭제곱
print(2 ** 8) # 256

#비교연산자
boolean1 = a == b
boolean2 = a == a
print(boolean1) # false
print(boolean2) # true
#동등비교
print(a == b) #false
#부등비교
print(a != b) #true

#크기비교
print(2 > 1) #True
print(2 < 1) #False
print(2 >= 1) #True
print(2 <= 1) #False

#논리연산자
#And연산자 두 조건 모두 참일 때만 참을 반환합니다
boolean4 = True and True
print(boolean4)  #True

boolean4 = True and False
print(boolean4) #False

#OR연산자 두 조건 중 하나라도 참이면 참을 반환합니다.
boolean = True or False
print(boolean) #True

boolean = False or False
print(boolean) # False

#논리NOT : 조건을 부정합니다.
boolean5 = not True
print(boolean5) #False

#연습하기
char1 = "안녕하세요"
char2 = "저는 이현우 입니다"
print(char1 + char2)
print(len(char1 + char2))

#input
# name = input("이름을 입력해 주세요")
# print("당신의 이름은" + name + "입니다") # 당신의 이름은이현우입니다

# age = input("당신의 나이를 입력해 주세요")
# age = int(age)  #input은 문자열만 입력 받는다 그렇기 때문에 정수형으로 변환 시켜야 한다
# print("당신의 이름은" + name + "이고 당신의 10년뒤 나이는" + str(age+10) +"입니다") 
#정수를 문자열과 결합하려면 str() 함수를 사용하여 정수를 문자열로 변환
#파이썬은 문자열과 숫자를 직접 연결할 수 없습니다

#format()
#메서드는 문자열 내에 변수나 값을 삽입하거나 형식화하는 데 사용되는 파이썬 문자열 메서드
#문자열 내에 중괄호 {}를 사용하여 변수나 값을 삽입하고
#중괄호 내에 인덱스나 변수 이름을 지정하여 값을 대체할 수 있다
name = "이현우"
age = 27
#기본형
message = "안녕하세요, {}님! 당신은 {}세입니다.".format(name, age)
#인덱스 사용
message = "안녕하세요, {0}님! 당신은 {1}세입니다.".format(name, age)
#이름을 사용한 변수 대체
message = "안녕하세요, {name}님! 당신은 {age}세입니다.".format(name=name, age=age)
print(message)

#형식 지정
#소수점 자릿수 지정 <.2f는 소수점 이하 2자리까지 출력하도록 지정>
price = 19.99
formatted_price = "상품 가격: ${:.2f}".format(price)
print(formatted_price)

# 정렬과 너비 지정 <{:>10}은 문자열을 오른쪽으로 정렬하고 총 10자리 너비를 갖도록 지정한 것.>
name = "Alice"
aligned_name = "{:>10}".format(name)
print(aligned_name)

#천 단위 구분 <,는 숫자를 출력할 때 천 단위마다 쉼표로 구분하도록 지정한 것>
number = 1000000
formatted_number = "{:,}".format(number)
print(formatted_number)

#진수, 16진수 등 다른 진법 출력 <b는 이진수로, :X는 대문자 16진수로 출력하도록 지정한 것>
number = 42
binary = "{:b}".format(number)
hex_value = "{:X}".format(number)
print("Binary: {}".format(binary))
print("Hex: {}".format(hex_value))

#if문
# 주어진 조건이 참(True)인 경우에만 특정 코드 블록을 실행
# number = int(input("아무 숫자를 입력해 주세요"))
if number > 0:
    print("0보다는 큽니다")
else:
    print("0보다는 작습니다")

#for 반복문
#파이썬에서 주어진 조건에 따라 일련의 작업을 반복적으로 수행하는 데 사용합니다
#fruits 리스트의 각 요소를 가져와서 화면에 출력합니다

#리스트 순회
햄버거 = ["치즈버거", "빅맥", "치킨버거"]
for 버거 in 햄버거:
    print(버거)

#범위를 이용한 반복 0부터 시작해서 range()까지
for i in range(10):
    print(i)

#문자열 순회
#문자열 text의 각 문자를 가져와서 공백이 아닌 경우에만 문자를 출력합니다
text = "안녕?, Python! 난 이현우야"
for char in text:
    if char != " ":
        print(char)

#while 반복문은 
#주어진 조건이 참(True)인 동안 반복적으로 코드 블록을 실행하는 데 사용
count = 1

while count <= 5:
    print(count)
    count += 1  # count를 1 증가

#입력문을 사용해서 while문 사용하기
answer = input("계속 진행하려면 'yes'를 입력하세요: ")
while answer == 'yes':
    print("프로그램을 계속 진행합니다.")
    answer = input("계속 진행하려면 'yes'를 입력하세요: ")

#python에서는 switch문이 없고 'if-elif-else'을 사용한다
#if-elif-else
choice = input("어떤 과일을 좋아하세요? (사과, 바나나, 오렌지): ")

if choice == "사과":
    print("사과를 선택하셨습니다.")
elif choice == "바나나":
    print("바나나를 선택하셨습니다.")
elif choice == "오렌지":
    print("오렌지를 선택하셨습니다.")
else:
    print("올바른 선택이 아닙니다.")

#while 반복문 안에 if-elif-else 구문을 사용
while True:
    choice = input("어떤 작업을 수행하시겠습니까? (예: 작업1, 작업2, 종료): ")

    if choice == "작업1":
        print("작업 1을 수행합니다.")
    elif choice == "작업2":
        print("작업 2를 수행합니다.")
    elif choice == "종료":
        print("프로그램을 종료합니다.")
        break  # while 루프를 종료합니다.
    else:
        print("올바른 선택이 아닙니다. 다시 입력하세요.")

#sorted() = 배열을 오름차순으로 정렬
numbers = [3, 7, 1, 9, 4]
sorted_numbers = sorted(numbers)
print("정렬 전:", numbers)
print("정렬 후:", sorted_numbers)

#reverse=True = 배열을 내림차순으로 정렬
numbers = [3, 7, 1, 9, 4]
sorted_numbers_descending = sorted(numbers, reverse=True)

print("정렬 전:", numbers)
print("내림차순 정렬 후:", sorted_numbers_descending)