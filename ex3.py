# Write and test a function Sort, which
# take two integers
# as parameters and returns them in ascending order
# (i.e. if x > y, then the function should return y, x).

def numbers():
    x = int(input("Please enter a number"))
    y = int(input("Please enter a number"))
    return x , y

def display(x , y):
    a = sorted(x , y)
    print(a)

        

        
numbers()    
display(x , y)
