import graph
from random import randrange


def black_left_column(width, height, length):
    for y in range(height):
        for x in range(width):
            if x < length:
                graph.plot(y, x)


def black_rectangle(x1, x2, y1, y2):
    for y in range(y1, y2):
        for x in range(x1, x2):
            graph.plot(y, x)


def inverted_rectangle(width, height, x1, x2, y1, y2):
    for y in range(height):
        for x in range(width):
            if (x < x1 or x > x2) or (y < y1 or y > y2):
                graph.plot(y, x)


def get_column_number(x, column_width):
    return x // column_width


def rayures_verticales(width, height, column_width):
    for y in range(height):
        for x in range(width):
            if get_column_number(x, column_width) % 2 != 0:
                graph.plot(y, x)


def damier(width, height, length):
    for y in range(height):
        offset = 0
        if get_column_number(y, length) % 2 != 0:
            offset = 1
        for x in range(width):
            if get_column_number(x, length) % 2 - offset != 0:
                graph.plot(y, x)


def get_random_color():
    random = randrange(9)
    if random == 0:
        return "red"
    elif random == 1:
        return "green"
    elif random == 2:
        return "blue"
    elif random == 3:
        return "yellow"
    elif random == 4:
        return "cyan"
    elif random == 5:
        return "magenta"
    elif random == 6:
        return "orange"
    elif random == 7:
        return "darkgrey"
    elif random == 8:
        return "black"


def rainbow_damier(width, height, length):
    cases = []
    last_column = -1
    for y in range(height):
        offset = 0
        y_column = get_column_number(y, length)
        if last_column != y_column:
            cases.append([get_random_color()])
            last_column = y_column
        if y_column % 2 != 0:
            offset = 1
        for x in range(width):
            x_column = get_column_number(x, length)
            if x_column == len(cases[y_column]):
                cases[y_column].append(get_random_color())
            if x_column % 2 - offset != 0:
                graph.plot(y, x, cases[y_column][x_column])


_width = 600
_height = 400
graph.ouvre_fenetre(_height, _width)

rainbow_damier(_width, _height, 50)

graph.attend_fenetre()
