import math

# Write a function which return the absolute value of the passed argument.
def abs_value(x):
    if x < 0:
        return -x
    return x


# Write a function which print a message which tell if the number is between 0 and 2pi.
def is_between_0_and_tau(x):
    if x >= 0 and x <= math.tau:
        print(str(x) + " is between 0 and 2pi")
    else:
        print(str(x) + " is not between 0 and 2pi")


# Write a function which tell between two numbers which is the biggest number.
def max(x, y):
    if x > y:
        return x
    return y


def max3(x, y, z):
    return max(x, max(y, z))


is_between_0_and_tau(abs_value(-1.5))
is_between_0_and_tau(3)
is_between_0_and_tau(5 * math.pi)
print(max(5, 2))
print(max3(2, 3, 4))

