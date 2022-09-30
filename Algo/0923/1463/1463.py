N = int(input())



def dfs(x)



for TC in range(T):
    Price_List = list(map(int, input().split()))
    Plan = list(map(int, input().split()))
    print(Price_List)
    # 가격 지정
    DP = Price_List[0]
    MP = Price_List[1]
    M3P = Price_List[2]
    YP = Price_List[3]
    check = [0 for i in range(n+1)]