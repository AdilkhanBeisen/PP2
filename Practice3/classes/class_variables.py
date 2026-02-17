# class_variables.py
# Demonstrates class variables vs instance variables


# Example 1
class Student:
    school = "KBTU"  # Class variable

    def __init__(self, name):
        self.name = name  # Instance variable

s1 = Student("Azamat")
s2 = Student("Ali")

print(s1.school)
print(s2.name)


# Example 2
class Car:
    wheels = 4  # Shared by all objects

    def __init__(self, brand):
        self.brand = brand

c1 = Car("BMW")
c2 = Car("Audi")

print(c1.wheels, c2.wheels)


# Example 3
class Company:
    company_name = "TechCorp"

    def __init__(self, employee):
        self.employee = employee

e1 = Company("John")
e2 = Company("Anna")

print(e1.company_name, e2.employee)


# Example 4
class Bank:
    interest_rate = 0.05  # Class variable

    def __init__(self, balance):
        self.balance = balance

b1 = Bank(1000)
b2 = Bank(2000)

print("Interest rate:", b1.interest_rate)
print("Balance:", b2.balance)