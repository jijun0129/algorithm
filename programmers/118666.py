def solution(survey, choices):
    answer = ''
    # 포인트를 저장할 dict 생성
    surveyPoint = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    # 각 선택지에 대한 포인트 계산
    for i in range(len(choices)):
        F, T = list(survey[i])
        point = choices[i] - 4
        if point > 0:
            surveyPoint[T] += point
        elif point < 0:
            surveyPoint[F] -= point
    
    # 각 포인트에 대한 선택지 계산
    if surveyPoint['R'] >= surveyPoint['T']:
        answer += 'R'
    else:
        answer += 'T'
    if surveyPoint['C'] >= surveyPoint['F']:
        answer += 'C'
    else:
        answer += 'F'
    if surveyPoint['J'] >= surveyPoint['M']:
        answer += 'J'
    else:
        answer += 'M'
    if surveyPoint['A'] >= surveyPoint['N']:
        answer += 'A'
    else:
        answer += 'N'
    
    return answer