def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
number = int(input("Enter a number: "))
factorial_result = factorial(number)
print("The factorial of", number, "is", factorial_result)
