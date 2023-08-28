str1 = input("Enter random string: ")

low = []
upp = [] 

for i in range(len(str1)):
    # if str1[i] >= 'a' and str1 <= 'z':
    if str1[i].islower():
        low.append(str1[i])
    # elif str1[i] >= 'A' and str1 <= 'Z':
    elif str1[i].isupper():
        upp.append(str1[i])

new = low + upp
new = ''.join(new)

print(new)