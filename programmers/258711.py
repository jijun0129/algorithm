from collections import defaultdict, deque

def solution(edges):
    # 추가한 정점, 도넛 모양, 막대 모양, 8자 모양
    answer = [0, 0, 0, 0]
    # dict의 기본값을 [0, 0]으로 설정(0: out-degree, 1: in-degree)
    degree = defaultdict(lambda: [0, 0])
    # dict의 기본값을 list로 설정
    graph = defaultdict(list)
    nodes = set()
    
    for a, b in edges:
        degree[a][0] += 1 # out-degree
        degree[b][1] += 1 # in-degree
        graph[a].append(b) # 그래프를 리스트로 추가
        nodes.add(a)
        nodes.add(b)

    # 추가한 정점은 out-degree가 2이 이상, in-degree가 0인 정점
    for key in degree: 
        if degree[key][0] >= 2 and degree[key][1] == 0:
            answer[0] = key
        
    visited = set()
    # 추가한 정점은 이미 방문한 것으로 처리 -> 계산 제외
    visited.add(answer[0])
    # BFS로 그래프에서 사이클, node 개수, edge 개수를 구한다.
    def bfs(start):
        queue = deque([start])
        visited.add(start)
        nodeCount = 0
        edgeCount = 0
        cycle = False

        while queue:
            q = queue.popleft()
            nodeCount += 1
            for neighbor in graph[q]:
                edgeCount += 1
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                elif neighbor == start:
                    cycle = True

        return nodeCount, edgeCount, cycle
    
    for node in nodes:
        if node not in visited:
            nodeCount, edgeCount, cycle = bfs(node)
            
            # 사이클이면서 edge 개수가 node 개수와 같다면 도넛 모양
            if cycle and edgeCount == nodeCount:
                answer[1] += 1
            # 사이클이 아니면서 edge 개수가 node 개수 - 1이면 막대 모양
            elif not cycle and edgeCount == nodeCount - 1:
                answer[2] += 1
            # 사이클이면서 edge 개수가 node 개수 + 1이면 8자 모양
            elif cycle and edgeCount == nodeCount + 1:
                answer[3] += 1
                
    return answer