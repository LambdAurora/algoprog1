from random import randrange


def a_la_chaine(n):
    return str_line(n, 'A')


def a_la_chaine_2(esp, n):
    return str_line_spaced(esp, n, 'A')


def str_line(length, c):
    result = c * length
    return result


def str_line_spaced(spaces, length, c):
    result = ' ' * spaces
    result += str_line(length, c)
    return result


def colonne(n):
    for i in range(10):
        print(a_la_chaine(n))


def diagonale1(n):
    for i in range(1, n + 1):
        print(a_la_chaine(i))


def diagonale2(n):
    for i in range(1, n + 1):
        print(a_la_chaine_2(n - i, i))


def sapin(n):
    for i in range(n):
        print(a_la_chaine_2(n - (i + 1), i + 1) + a_la_chaine(i))
    print(a_la_chaine_2(n - 2, 3))


def boule():
    aleatoire = randrange(100)
    if (aleatoire < 20):
        return 'O'
    return '*'


def sapin_decore(n):
    for i in range(n):
        result = ''
        for j in range(n - (i + 1)):
            result += ' '
        for j in range(2 * i + 1):
            result += boule()
        print(result)
    print(str_line_spaced(n - 2, 3, '*'))


sapin_decore(10)
