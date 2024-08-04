
def solution(answers):
    one, two, three = [], [], []
    score = [0 for _ in range(3)]
    while len(one) < len(answers):
        one += [1, 2, 3, 4, 5]
        two += [2, 1, 2, 3, 2, 4, 2, 5]
        three += [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answers)):
        if answers[i] == one[i]: score[0] += 1
        if answers[i] == two[i]: score[1] += 1
        if answers[i] == three[i]: score[2] += 1
    answer = []
    for i in range(len(score)):
        if score[i] == max(score):
            answer.append(i+1)
    return answer