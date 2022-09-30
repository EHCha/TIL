import sys
sys.stdin = open('1952.txt')


T = int(input())


for TC in range(T):
    Price_List = list(map(int, input().split()))
    Plan = list(map(int, input().split()))
    print(Price_List)
    # 가격 지정
    DP = Price_List[0]
    MP = Price_List[1]
    M3P = Price_List[2]
    YP = Price_List[3]