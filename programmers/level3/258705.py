def solution(n, tops):
    top = [0] * n
    bottom = [0] * n
    bottom[0] = 1
    # 위쪽 블럭은 삼각형 2개, 마름모 1개 + tops가 1이면 마름모 1개 -> 2개 or 3개
    top[0] = 2 + tops[0]
    
    for i in range(1, n):
        # top[i-1]에서 삼각형 더하기 + bottom[i-1]에서 마름모 더하기
        bottom[i] = (top[i-1] + bottom[i-1]) % 10007
        # top[i-1]에서 2 or 3(삼각형 2개, 마름모 2개 + tops가 1이면 마름모 1개) 곱하기
        # bottom[i-1]에서 1 or 2(삼각형 1개, tops가 1이면 마름모 1개) 곱하기
        top[i] = (top[i-1] * (2 + tops[i]) + bottom[i-1] * (1 + tops[i])) % 10007
        
    return (bottom[-1] + top[-1]) % 10007