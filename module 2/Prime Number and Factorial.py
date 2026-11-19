number = int(input("Enter a number: "))

# Prime number checking

if number < 2:
    print(number, "is not a prime number.")
else:
    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(number, "is a prime number.")
    else:
        print(number, "is not a prime number.")


# Factorial

factorial = 1

for i in range(1, number + 1):
    factorial = factorial * i

print("Factorial of", number, "is:", factorial)