n=int(input("Enter the size of tuple:"))
tup=[]

for i in range(n):
    x=input()
    tup.append(x)

tup=tuple(tup)

value=tup[0]

print( tup.count(value)==len(tup))
     