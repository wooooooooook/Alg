
def solution(genres: list, plays: list) -> list:
    answer = []
    gen = {}
    for i in range(len(genres)):
        if genres[i] not in gen:
            gen[genres[i]] = plays[i]
        else:
            gen[genres[i]] += plays[i]
    rank = list(gen.items())
    rank.sort(key=lambda x: x[1], reverse=True)
    print(rank)
    for i in range(len(rank)):
        index = []
        for j in range(len(genres)):
            if genres[j] == rank[i][0]:
                index.append([plays[j], j])
        index = sorted(index, key=lambda x: x[0], reverse=True)
        print(index)
        if len(index) == 1:
            answer.append(index[0][1])
        else:
            answer.append(index[0][1])
            answer.append(index[1][1])
    return answer