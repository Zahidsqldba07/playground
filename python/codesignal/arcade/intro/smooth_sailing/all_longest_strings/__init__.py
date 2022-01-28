def solution(input_array):
    longest = len(max(input_array, key=len))
    return [i for i in input_array if len(i) == longest]


print(solution(["aba", "aa", "ad", "vcd", "aba"]))
