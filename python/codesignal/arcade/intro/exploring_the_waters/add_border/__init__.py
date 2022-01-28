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
    length = len(picture)[0]
    picture.insert(0, ['*'] * (length + 2))


print(solution_02(["abc", "ded"]))
