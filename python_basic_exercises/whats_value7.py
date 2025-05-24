a = 1

def my_function():
    global a
    a = 2

my_function()
#highlight
print(a)       #prints 2
#global var assignment means we change the var a in all scopes of the program, local and global
#so the function will change the var and return it's new value
#this is not recommended
#endhighlight