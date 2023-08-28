string = input("Enter string")
sum=0
count=0
for i in range(len(string)):
    if(string[i].isdigit()):
       count=count+1
       num=int(string[i])
       sum=sum+num

avg=sum/count
print(sum)
print(avg)