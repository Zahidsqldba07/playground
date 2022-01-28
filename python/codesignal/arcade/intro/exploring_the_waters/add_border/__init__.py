def solution_01(picture):
    length = len(picture)
    width = len(picture[0])
    frame = [['*'] * (width + 2) for _ in range(length + 2)]
    new_picture = []

    for i in range(length):
        for j in range(width):
            frame[i + 1][j + 1] = picture[i][j]

    for i in range(length + 2):
        new_picture.append(''.join(frame[i]))

    return new_picture


def solution_02(picture):
    frame = '*' * (len(picture[0]) + 2)
    for i in range(len(picture)):
        picture[i] = '*' + picture[i] + '*'
    return [frame] + picture + [frame]


print(solution_02(["abc", "ded"]))
