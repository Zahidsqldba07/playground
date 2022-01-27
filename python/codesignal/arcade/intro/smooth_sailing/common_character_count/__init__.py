def solution(s1, s2):
    count = 0

    for i in s1:
        for j in range(len(s2)):
            if i == s2[j]:
                count += 1
                s2 = s2[:j] + s2[j+1:]
                break
    return count


print(solution("aabcc", "adcaa"))
