#parameter examples------------------------------------------------------------------------
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
# to call the function to return the string 'none'
#print(my_func3())



#aaaaargs examples - positional, kwargs, arbitrary---------------------------------------------------
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

# each arg in the fxn call will be added to 0 in loops and will loop through all args one at a time
print(sum_func2(10, 15))


# positional and kwargs
def my_func4(i,j):
    print(i,j)

my_func4(5,10) # positional args- same amount of args in same exact order
# my_func4(j=5,i=10) # kwargs- same amount of args in any order


#default values in positional arguments
def my_func5(i=10,j=15):
    print(i,j)

#passing a value that will replace the default value
my_func5(100)
#passing no values to return the default positional values
my_func5()


# mixing positional and kwargs
def my_func6(a,b,c):
    print(a,b,c)

my_func6(10,20,30) #by default this is positional args
my_func6(a=10,b=20,c=30)  #kwargs
my_func6(c=10,b=20,a=30) #kwargs
my_func6(10,20,c=30)
#my_func6(10,b=20,30) # syntax error because positional args should come before kwargs
#my_func6(a=10,30,b=20)  #type error (logic error)



# scope of variables -------------------------------------------------------------------

a = 100     #global var

def my_func():
    print(a)    #local var

my_func()

# modify the global variable locally
def my_func2():
    global a
    a=200
    print(a)

my_func2()
print(a)


#declare global var inside fxn
def my_func3():
    global x
    x=100
    print(x)

#call fxn
my_func3()
#now access x outside function
print(x)

