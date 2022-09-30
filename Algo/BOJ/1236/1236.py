import sys
sys.stdin = open('1236.txt')


N, M = map(int, input().split())

arr = [['.'] * N for _ in range(M)]
cnt = 0
for i in range(N):
    for j in range(M):
        # if 'X' not in arr[i][j]:
        #     cnt += 1
# print(cnt)
        print(arr[3])
