a=int(input("Enter the size of tuple 1 :"))
b=int(input("Enter the size of tuple 2 :"))

tup1=[]
tup2=[]

print("Enter thr elements in tuple 1:")
for i in range(a):
    x=input()
    tup1.append(x)
tup1=tuple(tup1)
print("Enter the elements in tuple 2:")
for i in range(b):
    x=input()
    tup2.append(x)
tup2=tuple(tup2)

print("Tuple 1 = ")
print(tup1)
print("Tuple 2 = ")
print(tup2)

temp=tup1
tup1=tup2
tup2=temp

print("After swapping the tuples we get,")
print("Tuple 1 = ")
print(tup1)
print("Tuple 2 = ")
print(tup2)
