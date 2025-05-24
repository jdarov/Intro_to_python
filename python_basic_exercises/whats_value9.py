a = 7

def my_function(b):
    b += 10

my_function(a)
#highlight
print(a)        #returns 7
#yet again, a function changes a var from param b in the local scope
#so a call to a will yet again only call the global var from program
#the global var remains at value 7
#endhighlight