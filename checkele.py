user_list = input("Enter a list of elements separated by spaces: ").split()

element = input("Enter the element to search for: ")
if element in user_list:
    print("The element", element, "exists in the list.")
else:
    print("The element", element, "does not exist in the list.")
