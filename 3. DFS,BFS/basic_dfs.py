def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]: # 현재 노드에서 갈 수 있는 곳 탐색
        if not visited[i]: # 방문했는지 확인
            dfs(graph, i, visited) # 방문 안 한 곳으로 이동하기

    # 갈림길인 현재 노드를 스택에 넣기
    # 방문 안 한 곳이 없을 경우
    # return
    # 스택 맨 위로 이동
    # 모두 방문했을 경우 스택에서 꺼내기
    # 스택이 비어 있으면 끝


# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2,3,8], # node 1과 연결된 곳
    [1,7], # node 2와 연결된 곳
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 dfs 함수 호출
dfs(graph, 1, visited)