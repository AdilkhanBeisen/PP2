
# Example 1
class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Azamat")
print(p1.name)


# Example 2
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

car1 = Car("Toyota", 2022)
print(car1.brand, car1.year)


# Example 3
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

s1 = Student("Ali", "A")
print(s1.name, s1.grade)


# Example 4
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

r = Rectangle(4, 5)
print("Length:", r.length, "Width:", r.width)