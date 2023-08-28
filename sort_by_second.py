n=int(input("Enter the size of tuple:"))
tup=[]
print("Enter the tuple:")
for i in range(n):
    x=input()
    tup.append(x)

m=int(input("Enter the size of list:"))
lst=[]
print("Enter the list:")

for i in range(m):
    x=input()
    lst.append(x)

pos=int(input("Enter the position where you want to insert element:"))
lst=tuple(lst)
tup.insert(pos, lst)

tup=tuple(tup)
print(tup)
for i in range(len(tup)):
    x=type(tup[i]) is tuple
    if x:
        tup[i][1]=sort(tup)
print(tup)        