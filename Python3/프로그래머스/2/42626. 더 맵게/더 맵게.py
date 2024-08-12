import heapq


def solution(scoville: list, K: int) -> int:
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        # 종료 조건 검사
        if len(scoville) <= 1:
            return -1
        heapq.heappush(scoville,
                       heapq.heappop(scoville) + heapq.heappop(scoville)*2)
        answer += 1
    return answer