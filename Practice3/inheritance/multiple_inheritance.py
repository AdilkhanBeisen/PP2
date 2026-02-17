
# Example 1
class Father:
    def skill1(self):
        return "Driving"

class Mother:
    def skill2(self):
        return "Cooking"

class Child(Father, Mother):
    pass

child = Child()
print(child.skill1(), child.skill2())


# Example 2
class Writer:
    def write(self):
        return "Writing"

class Speaker:
    def speak(self):
        return "Speaking"

class Person(Writer, Speaker):
    pass

p = Person()
print(p.write(), p.speak())


# Example 3
class A:
    def method_a(self):
        return "A method"

class B:
    def method_b(self):
        return "B method"

class C(A, B):
    pass

obj = C()
print(obj.method_a(), obj.method_b())


# Example 4
class Calculator:
    def add(self, a, b):
        return a + b

class Multiplier:
    def multiply(self, a, b):
        return a * b

class MathOperations(Calculator, Multiplier):
    pass

math = MathOperations()
print(math.add(2, 3), math.multiply(2, 3))