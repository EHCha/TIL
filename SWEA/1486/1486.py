T = int(input())


def min_sum(EN, height):
    global min_height

    if B <= height < min_height:
        min_height = height
    if EN == N:
        return
    min_sum(EN + 1, height)
    min_sum(EN + 1, height + arr[EN])


for TC in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    min_height = 200000
    min_sum(0, 0)

    print(f'#{TC} {min_height - B}')