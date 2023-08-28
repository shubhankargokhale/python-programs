
def insert(lst):
    pos=int(input("Enter the position where you have to add new element:"))
    ele=int(input("Enter the element:"))

    lst.insert(pos,ele)

lst=[]
n=int(input("Enter the number of elements in list:"))
print("Enter the elements:")
for i in range(1,n+1):
    k=input()
    lst.append(int(k))

insert(lst)
print("Therefore,new list is:")
print(lst)    