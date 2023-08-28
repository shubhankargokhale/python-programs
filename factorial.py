def fact(num):
    facto=1
    for i in range(1,num+1):
        facto=facto*i

    return facto

num=int(input("Enter the number:"))
print("The factorial of {0} is {1}".format(num,fact(num)))
