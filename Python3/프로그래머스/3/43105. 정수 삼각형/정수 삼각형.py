def solution(triangle):
    for i in range(len(triangle)-1):
        for j in range(i+2):
            # 첫 번째 값인 경우
            if j == 0:
                triangle[i+1][j] += triangle[i][j]
            # 마지막 값인 경우
            elif j == i+1:
                triangle[i+1][j] += triangle[i][j-1]
            # 부모 값 중 큰 값을 선택
            else:
                if triangle[i][j-1] < triangle[i][j]:
                    triangle[i+1][j] += triangle[i][j]
                else:
                    triangle[i+1][j] += triangle[i][j-1]
    return max(triangle[len(triangle)-1])