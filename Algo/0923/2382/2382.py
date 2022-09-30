import sys
sys.stdin = open('2382.txt')

T = int(input())

dx = [-1, 1, 0, 0]
dy = []
# def place_micro(xc, yc):


for tc in range(T):
    N, M, K = map(int, input().split())  # N = 정사각형 가로 세로 길이, M = 미생물 보관 시간, K= 미생물 군집수
    matrix = [[0 for _ in range(N)] for _ in range(N)]
    # print(matrix)

    for i in range(K):
        arr = list(map(int, input().split()))
        yc = arr[0]  # 세로 위치
        xc = arr[1]  # 가로 위치
        micro_num = arr[2]  # 미생물 수
        micro_dir = arr[3]  # 이동 방향
        
        # print(arr)









