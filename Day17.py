# 예외 처리 (Exception Handling) 예시

try:
    # 1. 나눗셈 예외 처리
    result = 10 / 0
except ZeroDivisionError as e:
    # 0으로 나눌 수 없을 때 실행됩니다.
    print("0으로 나눌 수 없습니다.")

try:
    # 2. 파일 읽기 예외 처리
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError as e:
    # 파일을 찾을 수 없을 때 실행됩니다.
    print("파일을 찾을 수 없습니다.")

try:
    # 3. 입력 유효성 검사 예외 처리
    age = int(input("나이를 입력하세요: "))
except ValueError as e:
    # 올바른 나이가 아닌 경우 실행됩니다.
    print("올바른 나이를 입력하세요.")

# 4. 사용자 정의 예외 처리
class CustomException(Exception):
    pass

try:
    raise CustomException("사용자 정의 예외 발생")
except CustomException as e:
    # 사용자 정의 예외가 발생한 경우 실행됩니다.
    print("사용자 정의 예외가 발생했습니다.")

try:
    # 5. 예외 처리의 마지막 부분 (finally)
    result = 10 / 0
except ZeroDivisionError as e:
    # 0으로 나눌 수 없을 때 실행됩니다.
    print("0으로 나눌 수 없습니다.")
finally:
    # 예외 처리가 종료되었을 때 실행됩니다.
    print("예외 처리가 종료되었습니다.")

# 패키지 정의와 설명 예시

# 1. 패키지 생성 및 모듈 정의
# bakery 패키지를 만들고 두 개의 모듈인 bread.py와 pastry.py를 포함합니다.

# 2. bread.py 모듈 예시
# bread 모듈에는 make_sandwich()와 make_toast() 함수가 정의되어 있습니다.

# 3. pastry.py 모듈 예시
# pastry 모듈에는 make_cookie()와 make_cake() 함수가 정의되어 있습니다.

# 4. 패키지 사용 예시
# bakery 패키지에서 bread 모듈과 pastry 모듈을 가져와 함수를 호출합니다.

# 이 모든 내용을 포함하는 완전한 코드입니다.
