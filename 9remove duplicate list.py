lst = [1, 2, 2, 3, 4, 4, 5, 1]
print("Original list:", lst)

new_lst = list(set(lst))
print("List after removing duplicates:", new_lst)
lst = []
if not lst:
    print("List is empty")
else:
    print("List is not empty")
lst = [1, 2, 3, 4, 5]
print("Original list:", lst)

new_lst = lst.copy()
print("Cloned list:", new_lst)




