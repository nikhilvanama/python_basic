def is_prime(n):
    if n == 1:
        return False

    if n == 2:
        return True

    for i in range(3, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
n = int(input("Enter a number: "))

if is_prime(n):
    print("The number is prime.")
else:
    print("The number is not prime.")