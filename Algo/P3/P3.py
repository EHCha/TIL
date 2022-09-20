import sys

sys.stdin = open('P3.txt')

pattern = {
    '001101': 0,
    '010011': 1,
    '111011': 2,
    '110001': 3,
    '100011': 4,
    '110111': 5,
    '001011': 6,
    '111101': 7,
    '011001': 8,
    '101111': 9,
}

T = int(input())
for _ in range(T):
    arr = input()
    M1 = ''

    for i in arr:
        N = int(i, 16)
        M = format(N, '04b')
        M1 += str(M)
    while M1:
        M2 = M1[:6]
        if M2 in pattern.keys():
            print(pattern[M2], end=" ")
            M1 = M1[6:]
        else:
            M1 = M1[1:]
    print()