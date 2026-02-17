
# Example 1
class Person:
    def greet(self):
        return "Hello!"

p = Person()
print(p.greet())


# Example 2
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

r = Rectangle(4, 5)
print("Area:", r.area())


# Example 3
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

account = BankAccount(100)
print("New balance:", account.deposit(50))


# Example 4
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def is_passed(self):
        return self.score >= 50

s = Student("Dana", 75)
print("Passed:", s.is_passed())