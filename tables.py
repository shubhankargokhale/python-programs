num = int(input("Enter a number:"))
print("Multiplication table of {0} is:".format(num))
for i in range(1,11):
    print("{0} x {1} = {2}".format(num,i,num*i))
