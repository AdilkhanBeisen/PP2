import datetime
# This program demonstrates different operations with dates and time
# Task 1: Subtract five days from current date
x = datetime.datetime.now()  # Get current date and time
new = x - datetime.timedelta(days=5)  # Subtract 5 days using timedelta
x=datetime.datetime.now()
new=x-datetime.timedelta(days=5) #timedelta differences in times, expressed in difference units
print(new)

# Task 2: Print yesterday, today and tomorrow

x = datetime.datetime.today()  # Get today's date and time
yest = x - datetime.timedelta(days=1)  # Calculate yesterday
tom = x + datetime.timedelta(days=1)  # Calculate tomorrow

print(f"Yesterday: {yest}")
print(f"Today: {x}")
print(f"Tommorow: {tom}")

# Task 3: Drop microseconds from current datetime

x = datetime.datetime.now()  # Get current datetime
print(x.replace(microsecond=0))  # Remove microseconds

# Task 4: Calculate difference between two dates in seconds
# Ask user to enter two dates in format YYYY-MM-DD HH:MM:SS

date1=input("Enter first date:")
date2=input("Enter second date")

date1_d = datetime.datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")  # Convert first input to datetime
date2_d = datetime.datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")  # Convert second input to datetime
#strptime() method, a string can be converted into a datetime

dif = abs((date1_d - date2_d).total_seconds())  # Calculate absolute difference in seconds

print("Difference:", int(dif))