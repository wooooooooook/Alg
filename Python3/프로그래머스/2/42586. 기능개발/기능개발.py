def solution(progresses, speeds):
    answer = []
    remain = len(progresses)
    count = 0
    pointer = 0
    while True:
        if remain <= 0:
            return answer
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        if progresses[pointer] >= 100:
            while True:
                remain -= 1
                count += 1
                pointer += 1
                if  pointer >= len(progresses):
                    break
                if not (progresses[pointer] >= 100):
                    break
            answer.append(count)
            count = 0