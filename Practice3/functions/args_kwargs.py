# Example 1: *args
def sum_all(*numbers):
    # Sums all positional arguments
    print("Total:", sum(numbers))


# Example 2: *args printing
def show_items(*items):
    # Prints each item
    for item in items:
        print(item)


# Example 3: **kwargs
def show_info(**info):
    # Prints dictionary of keyword arguments
    print(info)


# Example 4: **kwargs looping
def show_keys(**data):
    # Prints all keys
    for key in data:
        print("Key:", key)


# Calls
sum_all(1, 2, 3, 4)
show_items("apple", "banana")
show_info(name="Azamat", age=18)
show_keys(a=1, b=2)