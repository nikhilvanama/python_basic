user_list = input("Enter a list of elements separated by spaces: ").split()
unique_list = set(user_list)
num_unique = len(unique_list)
print("The number of unique elements in the list is:", num_unique)
