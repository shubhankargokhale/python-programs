def count(n):
    tup = []

    print("Enter the elements in tuple :")


    for i in range(n):
        x = input()
        tup.append(x)

    tup=tuple(tup)
    value = input("Enter the value:")

    num = tup.count(value)
    print("Frequency of {0} is {1} ".format(value, num))


n = int(input("Enter the size of tuple:"))
count(n)