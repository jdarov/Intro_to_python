x = 10

def my_function():
    #highlight
    # global x
    #endhighlight
    x = x + 5       #x is not defined in the local scope, so can not access global variable x (No params)
    print(x)   
#highlight
# x = 10
#endhighlight
my_function()  #this should print an error, as the global x can not be accessed in a local scope