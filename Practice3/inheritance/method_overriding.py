
# Example 1
class Animal:
    def speak(self):
        return "Animal sound"

class Cat(Animal):
    def speak(self):
        return "Meow"

c = Cat()
print(c.speak())


# Example 2
class Person:
    def role(self):
        return "General person"

class Student(Person):
    def role(self):
        return "Student"

s = Student()
print(s.role())


# Example 3
class Vehicle:
    def move(self):
        return "Moving"

class Bike(Vehicle):
    def move(self):
        return "Riding"

b = Bike()
print(b.move())


# Example 4
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def area(self):
        return 4 * 4

sq = Square()
print(sq.area())