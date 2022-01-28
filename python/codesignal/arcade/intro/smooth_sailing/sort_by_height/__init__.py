def solution(a):
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] != -1 and a[j] != -1 and a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    return a


print(solution([-1, 150, 190, 170, -1, -1, 160, 180]))
