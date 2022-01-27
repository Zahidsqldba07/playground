def solution(n):
    s = str(n)
    l = len(s)
    h = l // 2

    return l % 2 == 0 and sum(map(int, s[:h])) == sum(map(int, s[h:]))


print(solution(134008))
