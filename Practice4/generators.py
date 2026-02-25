# Task 1: Generate squares of numbers up to N
# This generator yields the square of each number from 0 to N-1
# Define generator function that returns squares
#Yield means to produce, provide, or give way.
def fun(max):
   for i in range(max):
       yield i**2 #means to produce the square of i and pause the function's execution, returning that value to the caller. 
n = int(input("Input num"))
gen=fun(n)
for i in gen:
    print(i)

# Task 2: Generate even numbers up to N
# This generator yields only even numbers from 0 to N-1
# Define generator function that returns even numbers

def even(num):
   for i in range(num):
       if i%2==0:
           yield i

n = int(input("Input num"))
gen=even(n)
for i in gen:
    print(i)

# Task 3: Generate numbers divisible by both 3 and 4
# This generator yields numbers that are divisible by 12
# Define generator function for numbers divisible by 3 and 4

def number(num):
   for i in range(num):
       if i%3==0 and i%4==0:
           yield i

n = int(input("Input num"))
gen=number(n)
for i in gen:
    print(i)

# Task 4: Generate squares between two numbers
# This generator yields squares from start (n) to end (m-1)
# Define generator function that returns squares in given range

def number(num,vum):
   for i in range(num,vum):
        yield i**2

n,m = list(map(int, input().split()))
gen=number(n,m)
for i in gen:
    print(i)

# Task 5: Generate numbers in reverse order
# This generator yields numbers from N down to 0
# Define generator function for reverse countdown

def down(num):
   for i in range(num,-1,-1):
    yield i

n = int(input("Input num"))
gen=down(n)
for i in gen:
    print(i)
