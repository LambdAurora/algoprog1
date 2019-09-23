import graph


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


width = 600
height = 400
graph.ouvre_fenetre(height, width)

inverted_rectangle(width, height, 150, 450, 50, 200)

graph.attend_fenetre()
