from collections import defaultdict 

def solution(n, wires):
    # 차이의 최소를 구한다. 
    min = n
    # 0부터 n-2의 wire를 하나씩 제거해본다. 
    for i in range(n-1):
        # 트리를 딕셔너리로 저장
        wireDict = defaultdict(list)
        for j in range(n-1):
            if i != j:
                a, b = wires[j]
                wireDict[a].append(b)
                wireDict[b].append(a)
        visited = [False] * (n+1)
        
        # 방문한 node를 True로 만든다. 
        def dfs(node):
            visited[node] = True
            for nextNode in wireDict[node]:
                if not visited[nextNode]:
                    dfs(nextNode)
                    
        dfs(1)
        # dfs를 한번 실행한 후 visited의 true수가 연결된 노드의 수
        count = 0
        for i in range(len(visited)):
            if visited[i]:
                count += 1
        
        # count와 n - count의 차이의 최소를 저장한다. 
        if abs(n - 2 * count) < min:
            min = abs(n - 2 * count)
    
    return min