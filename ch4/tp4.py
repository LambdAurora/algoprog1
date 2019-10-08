import graph


def get_some_numbers():
    """
    Gets numbers between 0 and 100 which are dividable by 2 or 3.
    :return: A list of those numbers.
    """
    result = []
    for i in range(100):
        if (i % 2) == 0 or (i % 3) == 0:
            result += [i]
    return result


def multiply_list(a_lst, n):
    result = []
    for n in lst:
        result += [n * 2]


def neighbor_pixels(x, y):
    """
    Gets coordinates of the neighbor pixels.
    :param x: The x current coordinate.
    :param y: The y current coordinate.
    :return: A list of the coordinates of the neighbor pixels.
    """
    result = []
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for d in directions:
        result += [(x + d[0], y + d[1])]
    return result


def get_column_number(x, column_width):
    return x // column_width


def get_image_width(a_lst, column_width):
    return column_width * len(a_lst)


def black_rectangle(x1, x2, y1, y2):
    for y in range(y1, y2):
        for x in range(x1, x2):
            graph.plot(y, x)


def draw_columns1(a_lst, height, column_width):
    graph.ouvre_fenetre(height, get_image_width(a_lst, column_width))
    for y in range(height):
        for x in range(get_image_width(a_lst, column_width)):
            if not a_lst[get_column_number(x, column_width)]:
                graph.plot(y, x)
    graph.attend_fenetre()


def draw_columns2(a_lst, height, column_width):
    graph.ouvre_fenetre(height, get_image_width(a_lst, column_width))
    for i in range(len(a_lst)):
        if not a_lst[i]:
            black_rectangle(i * column_width, i * column_width + column_width, 0, height)
    graph.attend_fenetre()


def count_lines(mtx):
    return len(mtx)


def count_columns(mtx):
    return len(mtx[0])


def get_image_size(mtx, size):
    return count_columns(mtx) * size, count_lines(mtx) * size


def draw_grid(mtx, size):
    image_size = get_image_size(mtx, size)
    graph.ouvre_fenetre(image_size[1], image_size[0])
    for i in range(count_lines(mtx)):
        for j in range(len(mtx[i])):
            if not mtx[i][j]:
                black_rectangle(j * size, j * size + size, i * size, i * size + size)
    graph.attend_fenetre()


lst = get_some_numbers()
print(lst)
for z in range(len(lst)):
    lst[z] *= 2
print(lst)

print(neighbor_pixels(4, 5))

lst = [1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0]
_height = 50
draw_columns1(lst, _height, 20)
draw_columns2(lst, _height, 20)

matrix = [[0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
          [0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
          [0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
          [0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
          [0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
          [0, 1, 1, 1, 1, 1, 0, 1, 1, 0],
          [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
draw_grid(matrix, 20)
