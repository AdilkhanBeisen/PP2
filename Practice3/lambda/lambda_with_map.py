
numbers = [1, 2, 3, 4]

# Multiply each number by 2
doubled = list(map(lambda x: x * 2, numbers))

# Add each number by 3
add=list(map(lambda x: x+3 , numbers))

# minus each number by 1
minus=list(map(lambda x: x-1 , numbers))

# divide  each number by 2
divide =list(map(lambda x: x//2 , numbers))


print(doubled)
print(add)
print(minus)
print(divide)