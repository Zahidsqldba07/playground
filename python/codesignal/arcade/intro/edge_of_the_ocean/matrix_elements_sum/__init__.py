def solution(matrix):
    rent = 0
    for section in range(len(matrix[0])):
        for room in range(len(matrix)):
            if matrix[room][section] == 0:
                # ghost found, exit the entire section below
                break
            rent += matrix[room][section]
    return rent


print(solution([
    [0, 1, 1, 2],
    [0, 5, 0, 0],
    [2, 0, 3, 3]
]))
