import sys
import heapq
sys.stdin = open('5250.txt')


# 출발에서 최종 도착지까지 경유하는 지역의 높이 차이에 따라 연료 소비량이 달라짐, 최적의 경로로 이동하면 최소한의 연료
# 인접 지역으로 이동시에는 기본적으로 1만큼의 연료가 들고, 더 높은 곳으로 이동하는 경우 높이 차이 만큼 추가로 연료가 소비


def min_path():
    q = []
    heapq.heappush(q, (0, 0, 0))
    distance[0][0] = 0

    dr = [1, 0,  ]
    dc = [0, 1,  ]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    for i in range(N):
        L = list(map(int, input().split()))
        distance = [[10000000 for _ in range(N)] * N for _ in range(N)]
