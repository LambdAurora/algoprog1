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
    return hanoi


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
    """
    Moves a number of blocks from the source to the destination.
    :param hanoi: The Hanoï towers.
    :param src: The source tower.
    :param dst: The destination tower.
    :param blocks: The number of blocks to move.
    :return:
    """
    if blocks == 0:
        return hanoi
    else:
        third = third_tower(src, dst)
        hanoi = hanoi_move(hanoi, src, third, blocks - 1)
        if not is_move_valid(hanoi, src, dst):
            return hanoi
        hanoi = move(hanoi, src, dst)
        hanoi = hanoi_move(hanoi, third, dst, blocks - 1)
        return hanoi


def hanoi_towers(hanoi, src, dst):
    blocks = len(hanoi[src])
    return hanoi_move(hanoi, src, dst, blocks)


hanoi_towers([[1, 2, 3, 4, 5], [6], []], 0, 2)
