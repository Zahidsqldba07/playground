def solution(picture):
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


print(solution(["abc", "ded"]))
