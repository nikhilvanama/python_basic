user_list = input("Enter a list of numbers separated by a space: ").split()

num_list = [int(num) for num in user_list]

for i in range(len(num_list)-2):
    if num_list[i] == num_list[i+1]-1 == num_list[i+2]-2:
        print("The list contains three consecutive numbers:", num_list[i:i+3])
        break
else:
    print("The list does not contain three consecutive numbers.")
