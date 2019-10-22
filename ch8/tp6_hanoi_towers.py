def third_tower(src, dst):
    if ((src == 0) and (dst == 1)) or ((src == 1) and (dst == 0)):
        return 2
    elif ((src == 0) and (dst == 2)) or ((src == 2) and (dst == 0)):
        return 1
    else:
        return 0


def display_move(src, dst):
    if src > dst:
        print("T" + str(dst) + " <= T" + str(src))
    else:
        print("T" + str(src) + " => T" + str(dst))


def move(hanoi, src, dst):
    b = hanoi[src][0]
    hanoi[src] = hanoi[src][1:]
    hanoi[dst] = [b] + hanoi[dst]
    display_move(src, dst)
    print(hanoi)


def is_move_valid(hanoi, src, dst):
    if not ((0 <= src <= 2) and (0 <= dst <= 2) and src != dst):
        print("src or dst is invalid")
        return False
    if len(hanoi[src]) == 0:
        print("src is empty")
        return False
    if len(hanoi[dst]) == 0:
        return True
    if hanoi[src][0] > hanoi[dst][0]:
        print("src is greater than dst")
        return False
    return True


def hanoi_move(hanoi, src, dst, blocks):
    if blocks == 0:
        return hanoi
    elif blocks == 1:
        if is_move_valid(hanoi, 0, 1):
            return move(hanoi, src, dst)
        return hanoi


move([[1, 2], [3], []], 0, 1)
