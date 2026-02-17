# Example 1
def greet(name="Guest"):
    # Uses default name if no argument is passed
    print("Hello,", name)


# Example 2
def power(base, exponent=2):
    # Raises base to exponent (default 2)
    print(base ** exponent)


# Example 3
def show_country(country="Kazakhstan"):
    # Displays country name
    print("Country:", country)


# Example 4
def multiply(a, b=10):
    # Multiplies a by b (default is 10)
    print(a * b)


# Calls
greet()
greet("Ali")

power(5)
power(5, 3)

show_country()
show_country("Japan")

multiply(5)
multiply(5, 2)

