
def solution(prices: list) -> list:
    answer = []
    for i in range(len(prices)):
        count = 0
        pointer = i+1
        for j in range(len(prices)-pointer):
            if prices[i] > prices[pointer]:
                count += 1
                break
            pointer += 1
            count += 1
        answer.append(count)
    return answer