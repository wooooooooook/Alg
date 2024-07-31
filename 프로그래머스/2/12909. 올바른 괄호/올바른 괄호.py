def solution(s: str) -> bool:
    stk = []
    for i in s:
        if i == "(":
            stk.append(i)
        else:
            try:
                if stk[-1] == ")":
                    return False
                else:
                    stk.pop()
            except IndexError:
                return False
    if len(stk) == 0:
        return True
    return False