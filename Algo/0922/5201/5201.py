import sys
sys.stdin = open('5201.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    weight = list(map(int, input().split()))
    capacity = list(map(int, input().split()))

    rst = 0
    weight.sort(reverse=True)
    capacity.sort(reverse=True)

    while True:

        if capacity[0] >= weight[0]:
            rst += weight[0]
            weight.remove(weight[0])
            capacity.remove(capacity[0])
        elif weight[0] > capacity[0]:
            weight.remove(weight[0])

        if len(weight) == 0 or len(capacity) == 0:
            break

    print(f'#{tc} {rst}')
