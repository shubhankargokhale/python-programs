def oddEven(num):
    if num%2==0:
        print("{0} is even.".format(num))
    else:
        print("{0} is odd".format(num))

num = int(input("Enter a number : "))
oddEven(num)

