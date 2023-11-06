# Get list from user
my_list = list(input("Enter elements separated by space: ").split())

# Get positions from user
pos1 = int(input("Enter first position to swap: "))
pos2 = int(input("Enter second position to swap: "))

# Access elements at the given positions
elem1 = my_list[pos1]
elem2 = my_list[pos2]

# Swap elements using temporary variable
temp = elem1
elem1 = elem2
elem2 = temp

# Update original list with swapped elements
my_list[pos1] = elem1
my_list[pos2] = elem2

# Print updated list
print("Updated list:", my_list)
