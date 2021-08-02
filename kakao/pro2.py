# 대기실은 5개이며, 각 대기실은 5x5 크기입니다.
# 거리두기를 위하여 응시자들 끼리는 맨해튼 거리가 2 이하로 앉지 말아 주세요.
# 단 응시자가 앉아있는 자리 사이가 파티션으로 막혀 있을 경우에는 허용합니다.
# 두 테이블 T1, T2가 행렬 (r1, c1), (r2, c2)에 각각 위치하고 있다면, T1, T2 사이의 맨해튼 거리는 |r1 - r2| + |c1 - c2| 입니다. ↩

# BFS or DFS 최단거리 구해서 return

def solution(places):
    answer = []

    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    visit = [[0] * 5 for _ in range(5)]
    print(visit)
    queue = [(0, 0)]

    while queue:
        x, y = queue.pop(0)

        if x == 4 and y == 4:
            # 최종 경로 도착
            print(visit[x][y])
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 4 and 0 <= ny < 4:
                if visit[nx][ny] == 0 and visit[nx][ny] == 'O':
                    visit[nx][ny] = visit[x][y] + 1
                    queue.append((nx, ny))

    return answer


templist = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"]
    , ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"]
    , ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"]
    , ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"]
    , ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

# solution(templist)
templist2 = []
for i in templist:
    for j in i:
        for q in j:
            print(q)

# POOOP
# OXXOX
# OPXPX
# OOXOX
# POXXP
