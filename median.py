user_list = input("Enter a list of numbers separated by spaces: ").split()
user_list = [int(i) for i in user_list] 

user_list.sort()
n = len(user_list)

if n % 2 == 0: 
    median = (user_list[n//2] + user_list[n//2 - 1])/2
else: 
    median = user_list[n//2]

print("The median of the list is:", median)

