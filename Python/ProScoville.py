# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
import heapq

def solution(scoville, k):
    answer = 0
    scoville.sort()
    while scoville[0] < k:

        if scoville.__len__() < 2 and scoville[0] < k:
            return -1

        f = heapq.heappop(scoville)
        s = heapq.heappop(scoville)
        answer = answer + 1
        heapq.heappush(scoville, f + (s * 2))
        print(scoville)

    return answer


temp = [1, 2, 3, 9, 10, 12]
k = 7

solution(temp, k)

