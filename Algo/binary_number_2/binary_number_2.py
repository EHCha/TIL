import sys
sys.stdin = open('binary_number_2.txt')

T = int(input())
for tc in range(1, T+1):
    N = float(input())
    rst = ""
    div = 1
    for _ in range(12):
        div = div * 0.5  # 점점 작아지는 2**-1
        if N - div >= 0:  # 빼 보았을시 0 보다 크다면
            rst += '1'  # rst에 정수 값을 주고
            N -= div  # N에 div를 빼준다
            if not N:  # 반복중 N의 값이 0 이된다면 break
                break
        else:
            rst += '0'  # 0 보다 작다면 rst에 0 추가

    if N:
        rst = 'overflow' # 12 번을 거치고도 아직 값이 남아있다면 overflow

    print(f'#{tc} {rst}')
