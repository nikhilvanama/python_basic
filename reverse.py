string = input("Enter a string: ")
def reverse_string(string, length):
    if length <= 1:
        return string
    else:
        return string[length-1] + reverse_string(string[:length-1], length-1)
reversed_string = reverse_string(string, len(string))
print("The reversed string is:", reversed_string)
