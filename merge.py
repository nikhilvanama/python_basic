list1 = input("Enter the first list (separate items by space): ").split()
list2 = input("Enter the second list (separate items by space): ").split()

merged_list = list1 + list2

print("Merged List:", merged_list)
for i in range(len(merged_list)):
    merged_list[i] = int(merged_list[i])
for i in range(len(merged_list)):
    for j in range(i+1, len(merged_list)):
        if merged_list[i] > merged_list[j]:
            temp = merged_list[i]
            merged_list[i] =merged_list[j]
            merged_list[j] = temp
print("Sorted list:", merged_list)


