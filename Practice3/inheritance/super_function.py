# super_function.py
# Demonstrates usage of super()


# Example 1
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

s = Student("Azamat", "A")
print(s.name, s.grade)


# Example 2
class Animal:
    def __init__(self, type):
        self.type = type

class Dog(Animal):
    def __init__(self, type, breed):
        super().__init__(type)
        self.breed = breed

d = Dog("Mammal", "Labrador")
print(d.type, d.breed)


# Example 3
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, year):
        super().__init__(brand)
        self.year = year

c = Car("Toyota", 2022)
print(c.brand, c.year)


# Example 4
class Shape:
    def __init__(self, name):
        self.name = name

class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

r = Rectangle("Rectangle", 4, 5)
print(r.name, r.width, r.height)