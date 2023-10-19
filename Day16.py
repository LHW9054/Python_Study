# buungeoppang.py

# 임포트의 기본적인 방법 (Importing)
import math
result = math.sqrt(25)
print(result)

import numpy as np
arr = np.array([1, 2, 3])
print(arr)

from datetime import datetime
now = datetime.now()
print(now)

# 클래스 정의 (Class Definition)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Alice", 30)
print(person1.name, person1.age)

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

circle1 = Circle(5)
print("원의 넓이:", circle1.area())

class Car:
    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

car1 = Car("Toyota", "Camry")
print(car1.wheels)
print(car1.make)

# 클래스 상속 (Inheritance)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "멍멍!"

class Cat(Animal):
    def speak(self):
        return "야옹!"

dog1 = Dog("멍멍이")
cat1 = Cat("야옹이")
print(dog1.name, dog1.speak())
print(cat1.name, cat1.speak())

class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        pass

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

circle2 = Circle("빨강", 5)
print(f"{circle2.color} 원의 넓이:", circle2.area())

class A:
    def method_A(self):
        print("메서드 A 호출")

class B:
    def method_B(self):
        print("메서드 B 호출")

class C(A, B):
    def method_C(self):
        print("메서드 C 호출")

obj_C = C()
obj_C.method_A()
obj_C.method_B()
obj_C.method_C()
