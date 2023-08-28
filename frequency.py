from collections import Counter
str="python is simple programming language"
str=list(str)
c=Counter(str)

for i in c:
    print(i, c[i])