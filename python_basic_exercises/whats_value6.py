a = 1

def my_function():
    # global a 
    a = 2

my_function()
#highlight
print(a)     #print 1
#first of all, my_function doesn't return a value
#however, this a scope issue
#the variable a is assigned in the local scope my_function;
#once the program runs, that variable is put aside
#and the global var will be used again instead
#endhighlight