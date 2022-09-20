import sys
sys.stdin = open('1240.txt')

mapping_code = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}

def find_pos():
    for i in range(N):
        for j in range(M - 1, -1, -1):
            if arr[i][j] == 1:
                return i, j


T = int(input())
for TC in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]

    sx, sy = find_pos()

    for i in range(8):
        sy -= 7
    sy += 1

    secret_code = []
    for i in range(8):
        secret_code.append(mapping_code.get(''.join(map(str, arr[sx][sy:sy + 7]))))
        sy += 7

    verifi_code = (secret_code[0] + secret_code[2] + secret_code[4] + secret_code[6]) * 3 \
                  + (secret_code[1] + secret_code[3] + secret_code[5] + secret_code[7])

    if verifi_code % 10 == 0:
        print(f'#{TC} {sum(secret_code)}')
    else:
        print(f'#{TC} 0')
