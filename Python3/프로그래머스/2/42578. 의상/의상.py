def solution(clothes):
    a = {}
    output = 1
    for i in clothes:
        if a.get(i[1]) == None:
            a[i[1]] = 1
        else:
            a[i[1]] += 1
    print(a)
    for i in a.values():
        output *= (i+1)
    return output-1