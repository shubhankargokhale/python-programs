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

tup.insert(pos, lst)

tup=tuple(tup)
print(tup)
for i in range(len(tup)):
    x=type(tup[i])is list
    if x:
        tup[i][0]*=10
print(tup)        