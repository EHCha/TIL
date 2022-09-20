import sys
sys.stdin = open('P1.txt')

T = int(input())

for _ in range(T):
    arr = input()
    while arr:
        new = arr[0:7]
        arr = arr[7:]
        rst = int(new, 2)
        print(rst, end=" ")
    print()
