def solution(participant, completion):
    output = {}
    for i in participant:
        if output.get(i) == None: output[i] = 1
        else: output[i] = output[i]+1
    for i in completion:
        output[i] = output[i]-1
        if output[i] == 0: del output[i]
    return list(output.keys())[0]
