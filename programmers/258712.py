def solution(friends, gifts):
    answer = [0] * len(friends)\
    # 이름을 index로 변환해주는 딕셔너리를 만든다
    nameIndex = {name:index for index, name in enumerate(friends)}
    # 서로 주고받은 선물의 개수를 2차원 배열로 계산
    giftTable = [[0] * len(friends) for _ in range(len(friends))]
    # 선물지수를 계산
    giftScore = [0] * len(friends)
    
    for gift in gifts:
        a, b = gift.split(' ')
        
        giftScore[nameIndex[a]] += 1
        giftScore[nameIndex[b]] -= 1
        
        giftTable[nameIndex[a]][nameIndex[b]] += 1
        
    # 서로 주고받은 선물의 개수를 비교하여 선물을 받을 사람을 결정
    for a in range(len(friends) - 1):
        for b in range(a, len(friends)):
            if giftTable[a][b] > giftTable[b][a]:
                answer[a] += 1
            elif giftTable[a][b] < giftTable[b][a]:
                answer[b] += 1
                
            else:
                if giftScore[a] > giftScore[b]:
                    answer[a] += 1
                elif giftScore[a] < giftScore[b]:
                    answer[b] += 1
    
    # 가장 많은 선물의 개수를 반환
    return max(answer)