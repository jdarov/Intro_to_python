a = 1

def my_function():
    print(a)
    a = 2
#highlight
my_function()   #returns Error : Program can't run
#here the variable is yet again attempted to assing locally
#however, the order doesn't matter
#so the code will return an error since we are trying to print a variable we dont assign until a line later
#this is equivalent of a single program with lines Print(x); x =1 in that order