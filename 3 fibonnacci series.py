num = int(input("enter digit :"))

def Fibonnacci(num):
    a=0
    b=1
    print(a)
    print(b)
    while(num!=0):
        c=a+b
        print(c)
        a=b
        b=c
        num=num-1

Fibonnacci(num)