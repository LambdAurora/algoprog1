# TP6: recursion
import math
import random


# Write a function which calculates the geometric progression without using the ** operator.
def geometric_progress(n, u0, q):
    if n == 0:
        return u0
    return q * geometric_progress(n - 1, u0, q)


def sum_one_on_squared_n(n):
    if n == 0:
        return 0
    return 1 / (n ** 2) + sum_one_on_squared_n(n - 1)


def random_list(n, max):
    if n == 0:
        return []
    return [random.randint(0, max)] + random_list(n - 1, max)


def path(lst, x):
    if not (x in lst):
        return []
    return lst[:1] + path(lst[1:], x)


def suppr_espaces_apost(txt):
    if len(txt) == 0:
        return ""
    elif (txt[0] == " ") or (txt[0] == "'"):
        return suppr_espaces_apost(txt[1:])
    return txt[0] + suppr_espaces_apost(txt[1:])


def is_palindrome(txt):
    txt = suppr_espaces_apost(txt)
    if len(txt) <= 1:
        return True
    return (txt[0] == txt[len(txt) - 1]) and is_palindrome(txt[1:len(txt) - 1])


def dichotomie_carre(bmin, bmax, epsilon):
    b = (bmin + bmax) / 2
    p = bmax - bmin
    if p <= epsilon:
        return bmin, bmax
    elif (bmin ** 2 - 2) * (b ** 2 - 2) < 0:
        return dichotomie_carre(bmin, b, epsilon)
    else:
        return dichotomie_carre(b, bmax, epsilon)


def dichotomie(f, bmin, bmax, epsilon):
    b = (bmin + bmax) / 2
    p = bmax - bmin
    if p <= epsilon:
        return bmin, bmax
    elif (f(bmin) * f(b)) < 0:
        return dichotomie(f, bmin, b, epsilon)
    else:
        return dichotomie(f, b, bmax, epsilon)


def squared_f(x):
    return x ** 2 - 2


assert geometric_progress(8, 3, 4) == (3 * 4 ** 8)
print(sum_one_on_squared_n(900) / ((math.pi ** 2) / 6) * 100)
print("Random list:", end=" ")
length = 10
lst = random_list(length, 1000)
print(lst, end=" ")
print("Length: " + str(len(lst)) + " (correct? " + str(len(lst) == length) + ")")
print(path([1, 4, 5, 6, 90, 5, 2, 8, 9, 7, 0], 2))
ex_str = "Hello World! I hope you feel good. I'll hug you if you need to."
print(ex_str + " => " + suppr_espaces_apost(ex_str))
print("nom: " + str(is_palindrome("nom")))
print("kayak: " + str(is_palindrome("kayak")))
print("hello: " + str(is_palindrome("hello")))
print("engage le jeu que je le gagne: " + str(is_palindrome("engage le jeu que je le gagne")))
print(str(dichotomie_carre(1, 2, 0.00001)) + " ; sqrt(2) == " + str(math.sqrt(2)))
print(dichotomie(squared_f, 1, 2, 0.00001))
