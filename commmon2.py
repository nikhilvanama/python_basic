list1 = list(input("Please enter the first list (elements separated by space): ").split())
list2 = list(input("Please enter the second list (elements separated by space): ").split())
common_lst = []
for item in list1:
    if item in list2:
        common_lst.append(item)

print("The common elements are:", common_lst)
