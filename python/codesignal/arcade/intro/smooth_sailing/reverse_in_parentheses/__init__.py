import re


def solution(inputString):
    m = re.search(r"\(([^()]*)\)", inputString)
    if m is None:
        return inputString
    return solution(inputString[: m.start()] + m.group(1)[::-1] + inputString[m.end():])


print(solution("(bar)"))
