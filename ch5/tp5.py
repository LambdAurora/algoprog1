def indice(lst, n):
    for i in range(len(lst)):
        if lst[i] == n:
            return i
    return None


def coord(laby, n):
    for y in range(len(laby)):
        for x in range(len(laby[y])):
            if laby[y][x] == n:
                return x, y
    return None


def is_lowercase(c):
    return 97 <= ord(c) <= 122


def decalage_car(c, n):
    new_ord = ord(c) + n
    if new_ord > 122:
        new_ord = new_ord - 122 + 97
    elif new_ord < 97:
        new_ord = new_ord - 97 + 122
    return chr(new_ord)


def decalage_str(str, n):
    result = ""
    for c in str:
        if is_lowercase(c):
            result += decalage_car(c, n)
        else:
            result += c
    return result


def decalage_fichier(in_file, out_file, n):
    file = open(in_file, "r")  # "r" = read
    content = file.read()
    file.close()
    content = decalage_str(content, n)
    file = open(out_file, "w") # "w" = write
    file.write(content)
    file.close()


matrix = [[1, 2, 3],
          [4, 5, 6]]
print(coord(matrix, 5))

a_file = "a_file.txt"
file = open(a_file, "w")
file.write("Hello world, I am a file!\nHow are you today? Because I feel very good.")
file.close()

decalage_fichier(a_file, "encoded_a_file.txt", 6)
decalage_fichier("encoded_a_file.txt", "decoded_a_file.txt", -6)
