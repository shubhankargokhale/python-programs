def fib(n):
    if n == 1:
        print(0)
    elif n == 2:
        print(0, 1)
    else:
        print(0, 1, end=' ')
        n1 = 0
        n2 = 1
        nth = n1 + n2
        while(n - 2 > 0):
            print(nth, end=' ')
            n1 = n2
            n2 = nth
            nth = n1 + n2
            n -= 1
        
n = int(input("Enter n (how many numbers you want to see in the series): "))
print("Fibonacci series of first {0} numbers is: ".format(n))
fib(n)