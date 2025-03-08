def solution(id_list, report, k):
    answer = []

    # 신고를 보낸사람을 저장하는 딕셔너리
    idDict = {}
    # 메일을 받는 횟수를 저장하는 딕셔너리
    countDict = {}

    # 딕셔너리를 초기화
    for ids in id_list:
        idDict[ids] = []
        countDict[ids] = 0
    
    # 신고를 받은 사람에 신고한 사람을 리스트로 저장
    for reportLine in report:
        send, receive = reportLine.split()
        idDict[receive].append(send)
        # 중복을 제거한다. (set을 이용)
        idDict[receive] = list(set(idDict[receive]))
        
    # k번 이상 신고를 받았을 때 메일을 보낸다. 
    for key in idDict:
        if len(idDict[key]) >= k:
            # 신고를 보낸사람에게 메일을 보낸다. 
            for ids in idDict[key]:
                countDict[ids] += 1
                
    for key in countDict:
        answer.append(countDict[key])
    return answer