import heapq
import sys

num = int(input())
q = []

for i in range(num):
    command = int(sys.stdin.readline())
    if command != 0:
        heapq.heappush(q, (-command))

    else:
        try:
            print(-1 * heapq.heappop(q))
        except:
            print(0)
