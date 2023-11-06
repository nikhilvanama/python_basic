# Ask the user to enter their list
user_list = input("Enter your list, separated by commas: ").split()

# Convert the user's inputs to integers (assuming the list contains only integers)
user_list = [int(x) for x in user_list]

# Print the original list
print("Original List: ", user_list)

# Assign the first and last elements of the list to temporary variables
first_element = user_list[0]
last_element = user_list[-1]

# Swap the first and last elements in the list using a temporary variable
user_list[0] = last_element
user_list[-1] = first_element

# Print the updated list
print("Updated List: ", user_list)
