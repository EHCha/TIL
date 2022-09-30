import sys
sys.stdin = open('1110.txt')

N = int(input()) # 26
New = N # 기존의 N을 새로운 변수로 받아주고
cnt = 0

while True:
    a = New // 10   # 2
    b = New % 10  # 6
    c = (a+b) % 10  # 8
    New = (b*10) + c
    cnt += 1
    if New == N:
        print(cnt)
        break







