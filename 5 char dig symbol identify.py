string=input("Enter anything:")
alphabets=digits=special=0

for i in range(len(string)):
    if(string[i].isalpha()):
        alphabets=alphabets+1
    elif(string[i].isdigit()):
        digits=digits+1
    else:
        special=special+1
        print("\n alp:",alphabets)
        print("\n dig:",digits)
        print("\n string:",special)
        