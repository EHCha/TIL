T = int(input())

for TC in range(1, T+1):
    N = int(input())
    X = N**(1/3)
    x = round(X)

    if x**3 == N:
        print(f'#{TC} {x}')
    else:
        print(f'#{TC} -1')