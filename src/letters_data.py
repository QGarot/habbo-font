data = [('a', 30), ('b', 30), ('c', 30), ('d', 30), ('e', 30), ('f', 30), ('g', 30), ('h', 30), ('i', 20), ('j', 28),
        ('k', 30), ('l', 28), ('m', 40), ('n', 30), ('o', 30), ('p', 30), ('q', 30), ('r', 30), ('s', 30), ('t', 30),
        ('u', 30), ('v', 30), ('w', 40), ('x', 30), ('y', 30), ('z', 30)]


def get_letter_size(x: str) -> int:
    if len(x) == 1:
        for letter, size in data:
            if letter == x:
                return size
        return 0
    else:
        return 0


def get_letter_index(x: str) -> int:
    i = 0
    if len(x) == 1:
        for letter, _ in data:
            if letter == x:
                return i
            else:
                i = i + 1


def get_letter_position(x: str) -> int:
    pos = 0
    for i in range(get_letter_index(x)):
        pos = pos + data[i][1] + 1
    return pos
