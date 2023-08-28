lst = ['Red', 'Green', 'White', 'Black', 'pink', 'Yellow']
print("Sample list: ", lst)


indices = [0, 4, 5]


new_lst = [lst[i] for i in range(len(lst)) if i not in indices]


print("Expected list: ", new_lst)

