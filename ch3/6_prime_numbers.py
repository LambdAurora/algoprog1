def is_prime_number(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def prime_numbers(n):
    for i in range(n):
        if is_prime_number(i):
            print(i)


print("is_prime_number(2) = " + str(is_prime_number(2)))
print("is_prime_number(3) = " + str(is_prime_number(3)))
print("is_prime_number(5) = " + str(is_prime_number(5)))
print("is_prime_number(6) = " + str(is_prime_number(6)))
print("is_prime_number(12) = " + str(is_prime_number(12)))
prime_numbers(100)

