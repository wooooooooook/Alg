
import heapq


def solution(jobs: list) -> int:
    jobs.sort()
    tick = 0
    wait = 0
    pros = []
    typ = len(jobs)
    queue = []
    while 1:
        # 종료 조건
        if not jobs and not queue and not pros:
            return wait//typ
        # 큐에 추가
        while jobs and tick == jobs[0][0]:
            tmp = heapq.heappop(jobs)
            heapq.heappush(queue, [tmp[1], tmp[0]])
        # 틱 증가
        tick += 1
        # 프로세스 추가
        if not pros and queue:
            tmp = heapq.heappop(queue)
            pros.append(tmp[0])
            pros.append(tmp[1])
        # 연산 수행
        if pros:
            pros[0] -= 1
            if pros[0] == 0:
                wait += tick-pros[1]
                pros.clear()