import graph

width = 200
img = graph.ouvre_fenetre(120, width)


def ligne_horiz(larg, y):
    for x in range(larg):
        graph.plot(y, x)


def segment_horiz(x1, x2, y):
    for x in range(x1, x2):
        graph.plot(y, x)


def rectangle(x1, x2, y1, y2):
    for y in range(y1, y2):
        segment_horiz(x1, x2, y)


def rayures_vertic(larg, height, larg_bande):
    x = larg_bande
    while x <= larg:
        rectangle(x, x + larg_bande, 0, height)
        x += 2 * larg_bande


def damier(width, height, cote):
    y = 0
    a = True
    while y < height:
        x = 0
        if a:
            x = cote
        while x < width:
            rectangle(x, x + cote, y, y + cote)
            x += 2 * cote
        y += cote
        a = not a


def sapin(large, haut):
    middle = int(large / 2)
    x = middle
    n = 1
    up_height = int(haut * 9 / 10)
    for y in range(1, up_height):
        for i in range(n):
            graph.plot(y, x + i)
        x -= 1
        if x < 0:
            up_height = y
            break
        n += 2
    rectangle(middle - 20, middle + 20, up_height, haut)


sapin(200, 110)

graph.attend_fenetre()
