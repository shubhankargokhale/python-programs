def max3(a,b,c):
    if (a>b):
        if a>c:
            print("{0} is greater".format(a))
        else:
            print("{0} is greater".format(c))
    else:
        if b>c:
            print("{0} is greater".format(b))
        else:
            print("{0} is greater".format(c))

a=int(input("Enter number 1 : "))
b=int(input("Enter number 2 : "))
c=int(input("Enter number 3 : "))

max3(a,b,c)       
