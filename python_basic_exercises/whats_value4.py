a = 1

def my_function():
    print(a)

my_function()  #LEGB Local, Enclosing, Global, Builtin
#in this code, it can't find local variable a, so it looks in enclosing, then in global
#global variable a = 1, so it will return 1. 
#if global a is assigned in this function, it will change all instances of var a