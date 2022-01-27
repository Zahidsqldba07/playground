def solution(statues):
    return max(statues) - min(statues) - len(statues) + 1


print(solution([6, 2, 3, 8]))
