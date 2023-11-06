user_list = list(map(int, input("Enter a list of integers: ").split()))

freq_dict = {}

for element in user_list:
    if element in freq_dict:
        freq_dict[element] += 1
    else:
        freq_dict[element] = 1
        
for element, count in freq_dict.items():
    print(element, "-", count, "times")
