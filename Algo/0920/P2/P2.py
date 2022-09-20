import sys
sys.stdin = open("P2.txt")

T = int(input())

for _ in range(T):
    arr = input()
    M1 = ''

    for i in arr:
        N = int(i, 16)
        M = format(N, '04b')
        M1 += str(M)

    while M1:
        new = M1[0:7]
        M1 = M1[7:]
        rst = int(new, 2)
        print(rst, end=" ")
    print()




# T = int(input())
#
# for _ in range(T):
#     arr = input()
#     M1 = ''
#     l = len(list(arr))
#     for i in range(l):
#         N = int(arr[i], 16)
#         M = format(N, '04b')
#         M1 += str(M)
#
#     while M1:
#         new = M1[0:7]
#         M1 = M1[7:]
#         rst = int(new, 2)
#         print(rst, end=" ")
#     print()

