def dfs(r,c,visited):
    # 현재 지점 방문 처리
    visited[r][c] = 1
    # 상하좌우로 이동하기
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    for d in range(4):
        nr, nc = r + directions[d][0], c + directions[d][1]
        if 0 <= nr < N and 0 <= nc < M: # 인덱스 에러 방지
            if icecream[nr][nc] == 0 and not visited[nr][nc]:
                dfs(nr,nc,visited)
    return result + 1

# 구멍 0 칸막이 1
# 세로 N 가로 M
# 한번에 만들 수 있는 아이스크림 개수
N, M = list(map(int, input().split()))
icecream = [list(input().split()) for _ in range(N)]
# 0 이 연결되어 있는 섬의 개수
# DFS
visited = [[0]*M for _ in range(N)]
result = 0
# 시작점에서 시작해서 모든 점을 순회할 때까지 처리하기
# 돌다가 0 을 만나면 dfs 안으로 들어가서 갈 수 있는 데까지 다 가보기
for r in range(M):
    for c in range(N):
        if icecream[r][c] == 0 and not visited[r][c]:
            result = dfs(r,c,visited)
print(result)