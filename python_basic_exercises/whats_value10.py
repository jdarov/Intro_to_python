b = [1, 2, 3]

def my_function():
    b[0] = 10
    # b = [10, 2, 3]

my_function()
#highlight
print(b)       #[10, 2, 3]
#this is a mutation of the original list, which affects every iteration of the var b
#a new var would keep it local scope and wouldn't change original list
#include an example of this where the list would remain untouched as it would assign a new list rather than
#mutate the old list, which affects every iteration of the var in the scope
#endhighlight