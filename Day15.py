# my_module.py

def add(a, b):
    return a + b

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, value):
        self.result += value

    def subtract(self, value):
        self.result -= value

    def get_result(self):
        return self.result

# 모듈을 불러옵니다.
import my_module

# 모듈 내의 함수를 사용합니다.
result = my_module.add(5, 3)
print("5 + 3 =", result)

# 모듈 내의 클래스를 사용합니다.
calc = my_module.Calculator()
calc.add(10)
calc.add(5)
calc.subtract(3)
calc_result = calc.get_result()
print("Calculator result:", calc_result)
