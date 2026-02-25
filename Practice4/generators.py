#1 task
def fun(max):
   for i in range(max):
       yield i**2

n = int(input("Input num"))
gen=fun(n)
for i in gen:
    print(i)

#2 task

def even(num):
   for i in range(num):
       if i%2==0:
           yield i

n = int(input("Input num"))
gen=even(n)
for i in gen:
    print(i)

#3 task

def number(num):
   for i in range(num):
       if i%3==0 and i%4==0:
           yield i

n = int(input("Input num"))
gen=number(n)
for i in gen:
    print(i)

#4 task

def number(num,vum):
   for i in range(num,vum):
        yield i**2

n,m = list(map(int, input().split()))
gen=number(n,m)
for i in gen:
    print(i)

#5 task
def down(num):
   for i in range(num,-1,-1):
    yield i

n = int(input("Input num"))
gen=down(n)
for i in gen:
    print(i)
