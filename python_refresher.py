#parameters
# example 1- fxn with no parameter and no return
def my_func():
    print("Hello")

my_func()


# example 2- fxn with parameter and no return
def my_func2(name):
    print("Hello", name)

# only pass the arguments when calling the fxn
my_func2("mishelle")


# example 3- fxn with parameters and returns the value
def cal(a,b):
    print(a+b)
    # return method: return (a+b)

# assign the values to a function to print the values
cal(5,10)
#return method means to assign the values to a variable and use the output elsewhere:
# sum = cal(5,10)


# example 4- returns none
def my_func3():
    return

# calling the function but not getting any output
my_func3()
# call the function to return the string 'none'
#print(my_func3())



#aaaaargs
# positional args
def sum_func(a,b):
    return a+b

print(sum_func(10, 15))


# arbitrary args (only tuple args)
def sum_func2(*numbers):
    total = 0
    for n in numbers:
        total = total + 1
    return total

# each arg in the fxn call will be added to 0 in one loop and will loop through all args one at a time
print(sum_func2(10, 15))


# positional and kwargs
def my_func4(i,j):
    print(i,j)

my_func4(5,10) # positional args- same amount of args in same exact order
# my_func4(j=5,i=10) # kwargs- same amount of args in any order
