# lambda_with_filter.py
# Using lambda with filter()

numbers = [5, 10, 15, 20]

# Filter numbers greater than 10
filtered = list(filter(lambda x: x > 10, numbers))
print(filtered)

# even numbers
filtered = list(filter(lambda x: x%2==0, numbers))
print(filtered)

#odd numbers
filtered = list(filter(lambda x: x%2==1, numbers))
print(filtered)
