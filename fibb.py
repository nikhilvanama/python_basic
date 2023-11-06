def is_fibonacci(number):
    a, b = 0, 1
    while a < number:
        a, b = b, a + b
    if a == number:
        return True
    else:
        return False
number = int(input("Enter a number: "))
if is_fibonacci(number):
    print(number, "is part of the Fibonacci series.")
else:
    print(number, "is not part of the Fibonacci series.")
