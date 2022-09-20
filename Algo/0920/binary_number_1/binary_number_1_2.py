import sys
sys.stdin = open('binary_number_1.txt')

T = int(input())

for TC in range(1, T+1):
    N, M = input().split()
    N = int(N)
    B = ''
    result = []
    for i in M:
        m = int(i, 16)
        NB = format(m, '04b')
        result.append(NB)
        result1 = ''.join(result)

    print(f'#{TC} {result1}')
