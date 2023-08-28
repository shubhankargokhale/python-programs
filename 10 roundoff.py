nums = [22.4, 4.0, 16.22, 9.10,  5.20 ,11.00, 17.50]
print("list=", nums)
numbers=list(map(round,nums))
print("Minimum = ",min(numbers))
print("Maximum = ",max(numbers))
numbers=list(set(numbers))


numbers=(sorted(map(lambda n:n*5,numbers)))

print("Ans:")
for numb in numbers:
    print(numb,end=' ')


import math
def specific_list(lst):
    for i in range(1,len(lst)):
        lst= math.ceil(lst[i])
    print(lst)       



# lst=[]
# n=int(input("Enter the number of elements in list:"))
# print("Enter the elements:")
# for i in range(1,n+1):
#     k=input()
#     lst.append(k)

# specific_list(lst)      