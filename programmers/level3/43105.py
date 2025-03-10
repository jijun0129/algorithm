def solution(triangle):
    # 맨끝의 한칸 위에서 시작해서 값을 구해간다. 
    # (i, j)에서 (i+1, j), (i+1, j+1) 중 큰 값으로 가야 최댓값이 된다. 
    for i in range(len(triangle)-2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
    # 마지막까지 수행후 맨 위의 값이 최댓값이 된다. 
    return triangle[0][0]