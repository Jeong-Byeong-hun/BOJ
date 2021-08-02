# 프린터 큐

from collections import deque

testNumber = int(input())

for _ in range(testNumber):
    n, x = map(int, input().split())
    que = deque(list(map(int, input().split())))
    idx_que = deque(list(range(n)))
    cnt = 0

    while que:
        if que[0] == max(que):
            cnt += 1
            que.popleft()
            if idx_que.popleft() == x:
                print(cnt)
        else:
            que.append(que.popleft())
            idx_que.append(idx_que.popleft())
