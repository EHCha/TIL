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
        B = bin(m)

        B = B.replace('0b',"")

        while True:
            if len(B) == 4:
                result.append(B)
                break
            else:
                B = '0'+B

    result1 = ''.join(result)
    print(f'#{TC} {result1}')



