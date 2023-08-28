def countt(str1):
    let = 0
    dig = 0
    spec = 0

    for i in range(len(str1)):
        if str1[i].isalpha():
            let += 1
        elif str1[i].isdigit():
            dig += 1
        else:
            spec += 1
    
    print("Chars = ", let)
    print("Digits = ", dig)
    print("Symbols = ", spec)

str1 = input("Enter random string: ")

countt(str1)