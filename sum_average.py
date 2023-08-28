def sum_avg(str1):
    digits = []

    for i in range(len(str1)):
        if str1[i].isdigit():
            digits.append(int(str1[i]))
    
    print(digits)

    summ = sum(digits)

    avg = summ/len(digits)

    print("Sum: ", summ)
    print("Average: ", avg)

str1 = input("Enter string: ")
sum_avg(str1)