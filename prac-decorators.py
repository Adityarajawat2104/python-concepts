# Funcations are represented as objects in Python

def f1():
    print("Hello")

# Functions can be passed as arguments to other functions
# def f2(f):
#     f()
#
# f2(f1)

# Define decorator function
def decfunc(func):
    def wrapper():
        print("Exec from wrapper")
        func()

    return wrapper

@decfunc
def f1():
    print("Hello")

f1()
# using decorator its like calling 2 funtions at the same time
# decorated function is passed as an argument to the function mentioned in decorator and called from within the main function


# Using decorator with arguments, the lower level function have arguments
def decfunc1(func):
    def wrapper(*args, **kwargs):
        print("Exec from wrapper2")
        func(*args, **kwargs)

    return wrapper

@decfunc1
def f2(a):
    print(a)

f2("Hello World")