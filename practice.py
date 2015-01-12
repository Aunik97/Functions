def get_input():
    while True:
        stars = int(input("enter how many stars that is an odd integer"))
        if stars % 2 and stars > 0:
            break
        else:
            print("{0} is not a positive odd integer".format(stars))


#main
get_input()
