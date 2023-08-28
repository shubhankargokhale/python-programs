import random

def rand(lst):
    n=int(input("How many elements you have to select randomly:"))
    ran= random.sample(lst, n)
    print("Therefore,Selected elements are",ran)

lst=[]
n=int(input("Enter the number of elements in list:"))
print("Enter the elements:")
for i in range(1,n+1):
    k=input()
    lst.append(k)

rand(lst)   
