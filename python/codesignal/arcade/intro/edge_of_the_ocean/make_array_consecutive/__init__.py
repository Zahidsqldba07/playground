def solution(sequence):
    droppped = False
    last = prev = min(sequence) - 1
    for elm in sequence:
        print(elm, prev, last)
        if elm <= last:
            if droppped:
                return False
            else:
                droppped = True
            if elm <= prev:
                prev = last
            elif elm >= prev:
                prev = last = elm
        else:
            prev, last = last, elm
    return True


print(solution([1, 3, 2, 1]))
