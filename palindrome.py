num = input("Enter a number: ")
str_num = str(num)
rev_num = str_num[::-1]

if str_num == rev_num:
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")
