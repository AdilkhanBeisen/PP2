
# Example 1
class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):
    pass

d = Dog()
print(d.speak())


# Example 2
class Person:
    def walk(self):
        return "Walking"

class Student(Person):
    pass

s = Student()
print(s.walk())


# Example 3
class Vehicle:
    def move(self):
        return "Moving"

class Car(Vehicle):
    pass

c = Car()
print(c.move())


# Example 4
class Shape:
    def info(self):
        return "This is a shape"

class Circle(Shape):
    pass

circle = Circle()
print(circle.info())