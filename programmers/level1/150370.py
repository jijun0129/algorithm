def solution(today, terms, privacies):
    answer = []
    # 오늘 날짜를 int형으로 분리하여 저장
    todayYear, todayMonth, todayDay = map(int, today.split('.'))
    
    # 약관을 저장한 딕셔너리를 생성하여 약관 종류로 유효기간을 찾도록 저장
    termDict = {}
    for term in terms:
        priName, priMonth = term.split(' ')
        termDict[priName] = int(priMonth)
        
    # 개인정보를 하나씩 확인
    for i in range(len(privacies)):
        priYMD, priName = privacies[i].split(' ')
        priYear, priMonth, priDay = map(int, priYMD.split('.'))
        # 유효기간을 더한다
        priMonth += termDict[priName]
            
        # 달이 12가 넘어간다면 빼면서 년도를 1씩 더해간다
        while priMonth > 12:
            priMonth -= 12
            priYear += 1
            
        # 더한 숫자와 같은 날짜까지는 파기해야한다. 
        # 1월 5일에서 3달 보관이라면 4월 4일까지 보관해야한다. (더한 숫자는 4월 5일)
        if priYear < todayYear:
            answer.append(i+1)
        elif priYear == todayYear and priMonth < todayMonth:
            answer.append(i+1)
        elif priYear == todayYear and priMonth == todayMonth and priDay <= todayDay:
            answer.append(i+1)
        
    return answer