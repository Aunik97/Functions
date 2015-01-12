def multiply(x, y):
    answer = x * y
    return answer

#main program
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
product = multiply(x, y)
print("The product of {0} X {1} is {2}".format(x, y, product))
